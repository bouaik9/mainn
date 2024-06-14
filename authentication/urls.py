from django.contrib import admin
from django.urls import path, include

from .views import loginform, home, signupview, logoutview

urlpatterns = [
    path('login/', loginform, name="login"),
    path('signup/', signupview, name="signup"),
    path('logout/', logoutview, name="logout")




    ]