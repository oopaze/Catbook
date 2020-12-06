from django.urls import path
from .views import IndexView, PublicacaoCreateView


urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('publicacao-create/', PublicacaoCreateView.as_view(), name="publicacao-create"),
]