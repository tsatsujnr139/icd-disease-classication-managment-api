from rest_framework import serializers

from core.models import DiseaseClassification


class DiseaseClassificationSerializer(serializers.ModelSerializer):
    """Serializer for Disease Classifications"""

    class Meta:
        model = DiseaseClassification
        fields = ("__all__")
        read_only_fields = ('id',)
