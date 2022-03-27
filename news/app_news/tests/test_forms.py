from django.test import TestCase
from ..forms import RegisterForm, ProfileForm, AuthForm


class RegisterFormTest(TestCase):

    def test_form_field_label(self):
        form = RegisterForm()
        # print('********', form.fields['first_name'].help_text, flush=True)
        self.assertTrue(form.fields['first_name'].help_text == 'Имя')


class AuthFormTest(TestCase):

    def test_weak_password(self):
        form = AuthForm({'username': 'username', 'password': '123'})
        # print('********', form.fields['first_name'].help_text, flush=True)
        self.assertFalse(form.is_valid() == False)


class ProfileFormTest(TestCase):

    def test_form_field_disabled(self):
        form = ProfileForm()
        self.assertTrue(form.fields['is_verified'].disabled)