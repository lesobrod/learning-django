import os
from pathlib import Path
from django.conf import settings
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views.generic import ListView, View, CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.core.cache import cache
from django import forms
from .models import News, Comment, Profile, NewsImage
from .forms import CommentForm, EditCreateForm, RegisterForm, \
    ProfileForm, MultiFileForm, UploadNewsForm
from django.forms.models import model_to_dict


class NewsListView(ListView):
    model = News
    template_name = 'app_news/index.html'
    context_object_name = 'all_news'

    def get_context_data(self, **kwargs):
        context = super(NewsListView, self).get_context_data(**kwargs)

        # Кнопки создания и редактирования новости отображаются только для авторизованных
        # Это поле is_verified в Profile
        # Но если у пользователя нет профиля, будет ошибка
        try:
            user_profile = Profile.objects.get(user_id=self.request.user.id)
            context['is_verified'] = user_profile.is_verified
        except Profile.DoesNotExist:
            context['is_verified'] = False
        return context


class NewsDetailView(TemplateView):
    model = News
    template_name = 'app_news/news_detail.html'

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        context = self.get_context_data(**kwargs)
        obj = comment_form.save(commit=False)
        if comment_form.is_valid():
            if request.user.is_authenticated:
                obj.user = request.user
                obj.author = request.user.username
            else:
                obj.author += ' (Аноним)'

            obj.save()

        return super(TemplateView, self).render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        # Получаем объект новости
        current_news = News.objects.get(id=kwargs['news_id'])
        context['news'] = current_news

        # Получаем картинки к новости и кэшируем их
        cached_pictures_key = 'cached_pictures:{}'.format(kwargs['news_id'])
        pictures = NewsImage.objects.filter(news=current_news)
        cache.get_or_set(cached_pictures_key, pictures, 30 * 60)
        context['pictures'] = pictures

        # Получаем все каменты к ней
        context['comments'] = Comment.objects.all().filter(news=kwargs['news_id'])
        # Индекс новости камента совпадает с индексом данной новости
        comment_form = CommentForm(initial={'news': kwargs['news_id']})
        # Поэтому просто убираем выбор новости
        comment_form.fields['news'].widget = forms.HiddenInput()
        comment_form.fields['user'].widget = forms.HiddenInput()
        if self.request.user.is_authenticated:
            comment_form.fields['author'].widget = forms.HiddenInput()

        context['comment_form'] = comment_form
        return context


class NewsCreateView(TemplateView):
    model = News
    template_name = 'app_news/news_create.html'

    def post(self, request, *args, **kwargs):
        create_form = EditCreateForm(request.POST)
        upload_files_form = MultiFileForm(request.POST, request.FILES)
        context = self.get_context_data(**kwargs)
        created_news = None
        if "main_form" in request.POST:
            if create_form.is_valid():
                created_news = create_form.save()

        if "image_form" in request.POST:
            if created_news:
                files = request.FILES.getlist('file_field')
                for f in files:
                    file_instance = NewsImage(images=f, news=created_news)
                    file_instance.save()
                return redirect('index')

        return super(TemplateView, self).render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(NewsCreateView, self).get_context_data(**kwargs)
        create_form = EditCreateForm(initial={'status': '3'})
        upload_files_form = MultiFileForm(self.request.POST, self.request.FILES)
        context['create_form'] = create_form
        context['upload_files_form'] = upload_files_form
        return context


class NewsEditView(TemplateView):
    model = News
    template_name = 'app_news/news_edit.html'

    def post(self, request, *args, **kwargs):
        current_news = News.objects.get(pk=kwargs['news_id'])
        edit_form = EditCreateForm(request.POST, instance=current_news)
        upload_files_form = MultiFileForm(request.POST, request.FILES)
        context = self.get_context_data(**kwargs)
        if "main_form" in request.POST:
            if edit_form.is_valid():
                edit_form.save()

        if "image_form" in request.POST:
            files = request.FILES.getlist('file_field')
            for f in files:
                file_instance = NewsImage(images=f, news=current_news)
                file_instance.save()
            return redirect('index')

        return super(TemplateView, self).render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(NewsEditView, self).get_context_data(**kwargs)
        current_news = News.objects.get(id=kwargs['news_id'])
        context['news'] = current_news
        edit_form = EditCreateForm(initial=
                                   model_to_dict(current_news))
        upload_files_form = MultiFileForm(self.request.POST, self.request.FILES)
        context['edit_form'] = edit_form
        context['upload_files_form'] = upload_files_form
        return context


class NewsLoginView(LoginView):
    template_name = 'app_news/login.html'


class NewsLogoutView(LogoutView):
    template_name = 'app_news/logout.html'


class NewsRegisterView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('index')
    template_name = 'app_news/register.html'


class NewsProfileView(UpdateView):
    form_class = ProfileForm
    model = get_user_model()
    success_url = reverse_lazy('index')
    template_name = 'app_news/profile.html'

    def get_context_data(self, **kwargs):
        context = super(NewsProfileView, self).get_context_data(**kwargs)

        try:
            user_profile = Profile.objects.get(user_id=self.request.user.id)
            context['is_verified'] = user_profile.is_verified
        except Profile.DoesNotExist:
            context['is_verified'] = False
        return context


class NewsStartView(TemplateView):
    template_name = 'app_news/start.html'


class NewsUploadView(TemplateView):
    template_name = 'app_news/news_upload.html'

    def post(self, request, *args, **kwargs):
        upload_form = UploadNewsForm(request.POST, request.FILES)
        create_form = EditCreateForm()
        context = self.get_context_data(**kwargs)
        if upload_form.is_valid():
            upload_news = upload_form.cleaned_data['file_field'].read()
            obj = create_form.save(commit=False)
            obj.title = 'Test'
            obj.description = upload_news.decode('utf-8')
            obj.save()
            return redirect('index')
        return super(TemplateView, self).render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(NewsUploadView, self).get_context_data(**kwargs)
        upload_form = UploadNewsForm(self.request.POST, self.request.FILES)
        context['upload_form'] = upload_form
        return context
