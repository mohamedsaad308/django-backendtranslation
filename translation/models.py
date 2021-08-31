from django.db import models
from model_utils.models import TimeStampedModel
# Create your models here.
# Translations


class NAMESPACE(models.TextChoices):
    COMMON = 'common'
    ERRORS = 'errors'
    TRANSLATION = 'translation'


class LANGUAGE(models.TextChoices):
    ARABIC = "ar"
    ENGLISH = "en"


class TranslationKey(TimeStampedModel):
    name = models.CharField(max_length=1024)
    namespace = models.CharField(
        max_length=15,
        choices=NAMESPACE.choices,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'namespace'], name='Translation key')
        ]

    def __str__(self):
        return f"namespace: {self.namespace}, Key: {self.name}"


class Translation(TimeStampedModel):
    translation_key = models.ForeignKey(
        TranslationKey, on_delete=models.CASCADE)
    language = models.CharField(
        max_length=10,
        choices=LANGUAGE.choices,
    )
    value = models.TextField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['translation_key', 'language'], name='Translation Value')
        ]
