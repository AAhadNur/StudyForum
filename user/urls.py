
from django.urls import path

from user.views import loginPage, logoutUser, registerPage

urlpatterns = [
    path('login/', loginPage, name="login"),

    path('logout/', logoutUser, name="logout"),

    path('signup/', registerPage, name="signup"),
]
