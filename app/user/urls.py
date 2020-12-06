from django.urls import path
from .views import UserLoginView, UserLogoutView, UserCreateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='create-user')
]
