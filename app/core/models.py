from django.db import models

# Create your models here.


class DiseaseClassification(models.Model):
    """Model definition for Disease Classification"""
    classification_standard = models.CharField(
        max_length=6, blank=False)
    category_code = models.CharField(max_length=4, blank=False)
    diagnosis_code = models.CharField(max_length=4, null=True)
    full_code = models.CharField(
        max_length=7, unique=True, blank=False)
    abbreviated_description = models.CharField(
        max_length=150, blank=False)
    full_description = models.CharField(max_length=255, blank=False)
    category_title = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.full_code
