from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Comment, News, Profile
from django.forms.widgets import HiddenInput


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80, 'rows': 10}),
        }


class EditCreateForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
        exclude = ['admin_comment', 'age_rate']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 10}),
        }


class UploadNewsForm(forms.Form):
    file_field = forms.FileField()


class MultiFileForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Имя')
    last_name = forms.CharField(max_length=30, required=False, help_text='Фамилия')

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_verified'].disabled = True
        self.fields['user'].widget = HiddenInput()
