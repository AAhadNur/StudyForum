
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from user.models import CustomUser


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'username', 'email', 'password1', 'password2']


class UserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['avatar', 'name', 'username', 'email', 'bio']
