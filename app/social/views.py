from django.shortcuts import render
from django.views.generic import ListView
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

