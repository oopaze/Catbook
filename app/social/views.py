from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from tabelas.models import Publicacao
from .forms import PublicacaoForm


class IndexView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    model = Publicacao  
    context_object_name = 'publicacoes'
    pagination = 20

    def get_queryset(self, *args, **kwargs):
        qs = self.model.objects.filter(user = self.request.user).all()
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['form'] = PublicacaoForm
        return context


class PublicacaoCreateView(LoginRequiredMixin, CreateView):
    model = Publicacao
    form_class = PublicacaoForm
    success_url = reverse_lazy("home")

    def get(self, *args, **kwargs):
        super().get(*args, **kwargs)
        return redirect(self.success_url)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
