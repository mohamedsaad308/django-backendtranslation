from django.contrib import admin
from django.contrib import admin
from .models import TranslationKey, Translation
from .forms import AtLeastOneRequiredInlineFormSet
# Register your models here.


class TranslationInline(admin.TabularInline):
    model = Translation
    formset = AtLeastOneRequiredInlineFormSet


class TranslationKeyAdmin(admin.ModelAdmin):
    inlines = [
        TranslationInline
    ]


admin.site.register(TranslationKey, TranslationKeyAdmin)
