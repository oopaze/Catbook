from django.shortcuts import render
from django.views.generic import RedirectView, FormView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib.auth import logout

from  .forms import UserAuthenticationForm

class UserLogoutView(RedirectView):
    url = reverse_lazy('login')

    def post(self, request, *args, **kwargs):
        logout(request)
        return super().post(request, *args, **kwargs)


class UserLoginView(auth_views.LoginView):
    template_name = 'user/login.html'
    authentication_form = UserAuthenticationForm