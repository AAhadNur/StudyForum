
from django.contrib.auth.forms import UserCreationForm

from user.models import CustomUser


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'username', 'email', 'password1', 'password2']
