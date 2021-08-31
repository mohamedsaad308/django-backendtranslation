from .models import TranslationKey, Translation
from rest_framework import serializers


class TranslationKeySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TranslationKey
        fields = ['name', 'namespace']
        read_only_fields = ['namespace', 'name']


class TranslationSerializer(serializers.HyperlinkedModelSerializer):
    translation_key = serializers.PrimaryKeyRelatedField(
        queryset=TranslationKey.objects.filter())

    class Meta:
        model = Translation
        fields = ['translation_key', 'language', 'value']
