from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.NewsListView.as_view(), name='main'),
                  path('index/', views.NewsListView.as_view(), name='index'),

                  path('app_news/news_detail/<int:news_id>',
                       views.NewsDetailView.as_view(),
                       name='news_detail'),

                  path('app_news/start/',
                       views.NewsStartView.as_view(),
                       name='start'),

                  path('app_news/news_create/',
                       views.NewsCreateView.as_view(),
                       name='news_create'),

                  path('app_news/news_upload/',
                       views.NewsUploadView.as_view(),
                       name='news_upload'),

                  path('app_news/news_edit/<int:news_id>',
                       views.NewsEditView.as_view(),
                       name='news_edit'),

                  path('app_news/login/',
                       views.NewsLoginView.as_view(),
                       name='login'),

                  path('app_news/logout/>',
                       views.NewsLogoutView.as_view(),
                       name='logout'),

                  path('app_news/register/',
                       views.NewsRegisterView.as_view(),
                       name='register'),

                  path('app_news/profile/<slug:pk>/',
                       views.NewsProfileView.as_view(),
                       name='profile'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
