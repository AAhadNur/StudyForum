
from django.urls import path

from user.views import loginPage, logoutUser, registerPage, userProfile, updateUser

urlpatterns = [
    path('login/', loginPage, name="login"),

    path('logout/', logoutUser, name="logout"),

    path('signup/', registerPage, name="register"),

    path('profile/<str:pk>/', userProfile, name="user-profile"),

    path('update-user/', updateUser, name="update-user"),
]
