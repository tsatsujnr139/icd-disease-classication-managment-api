from rest_framework import viewsets, mixins, pagination

from disease_classification.serializers import DiseaseClassificationSerializer


from core.models import DiseaseClassification


class DiseaseClassificationViewSet(viewsets.GenericViewSet,
                                   mixins.ListModelMixin,
                                   mixins.CreateModelMixin,
                                   mixins.RetrieveModelMixin,
                                   mixins.UpdateModelMixin,
                                   mixins.DestroyModelMixin):
    serializer_class = DiseaseClassificationSerializer
    pagination_class = pagination.api_settings.DEFAULT_PAGINATION_CLASS
    queryset = DiseaseClassification.objects.all().order_by('id')
    lookup_field = ('id')
