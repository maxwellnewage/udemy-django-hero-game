from django.forms import ModelForm, CharField, PasswordInput
from app.models import User
from django.contrib.auth.forms import UserCreationForm


class UserLoginForm(ModelForm):
    password = CharField(widget=PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
