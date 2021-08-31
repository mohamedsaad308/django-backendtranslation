from rest_framework import mixins, viewsets
from rest_framework.status import HTTP_204_NO_CONTENT
from django.http import JsonResponse, HttpResponse
from .serializers import TranslationKeySerializer, TranslationSerializer
from .models import TranslationKey, Translation
# Create your views here.


class TranslationKeyViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    API endpoint that allow adding missing translation keys
    """
    serializer_class = TranslationKeySerializer
    queryset = TranslationKey.objects.all()

    def perform_create(self, serializer):
        ns = self.request.query_params.get('ns')
        key_name = list(self.request.data.keys())[0]
        trans_key = TranslationKey.objects.filter(
            name=key_name, namespace=ns).first()
        if trans_key:
            return HttpResponse({}, HTTP_204_NO_CONTENT)
        # magic here: add kwargs for extra fields to write to db
        serializer.save(name=key_name, namespace=ns)


class TranslationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows translations to be viewed or edited.
    """
    serializer_class = TranslationSerializer
    queryset = Translation.objects.all()

    def list(self, request, *args, **kwargs):
        """
        Returned JSON structure in the format
        {
         lang : {
          namespaceA: {},
          namespaceB: {},
          ...etc
         }
        }      
        """
        namespaces = request.query_params.get('ns').split(' ')
        lngs = request.query_params.get('lng').split(' ')
        queryset = Translation.objects.filter(translation_key__namespace__in=namespaces, language__in=lngs).select_related(
            'translation_key')
        data = {}
        for lng in lngs:
            data[lng] = {}
            for ns in namespaces:
                data[lng][ns] = dict((query.translation_key.name, query.value)
                                     for query in queryset if query.language == lng and query.translation_key.namespace == ns)
        return JsonResponse(data)
