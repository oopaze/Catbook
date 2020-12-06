from django.shortcuts import render, redirect
from django.views.generic import RedirectView, FormView, CreateView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib.auth import logout

from .forms import UserAuthenticationForm, UserCreateForm
from tabelas.models import User 

class UserLogoutView(RedirectView):
    url = reverse_lazy('login')

    def post(self, request, *args, **kwargs):
        logout(request)
        return super().post(request, *args, **kwargs)


class UserLoginView(auth_views.LoginView):
    template_name = 'user/login.html'
    authentication_form = UserAuthenticationForm
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['register_form'] = UserCreateForm
        return context


class UserCreateView(CreateView):
    model = User
    form_class = UserCreateForm
    success_url = reverse_lazy('home')

    def get(self, *args, **kwargs):
        return redirect(reverse_lazy('login'))