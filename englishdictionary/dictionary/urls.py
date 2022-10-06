from django.urls import path
from .views import index_view, word_view

urlpatterns = [
    path('', index_view, name = 'index'),
    path('word', word_view, name = 'word'),
]
