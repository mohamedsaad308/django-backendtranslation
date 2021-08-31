from django.urls import path
from .views import TranslationKeyViewSet, TranslationViewSet
from rest_framework import routers
from . import views
app_name = 'translation'


urlpatterns = [
    path('translations/',
         view=TranslationViewSet.as_view({'get': 'list'}), name='translations'),
    path('translation_keys/', view=TranslationKeyViewSet.as_view({'post': 'create'}),
         name='translation_keys'),
]
