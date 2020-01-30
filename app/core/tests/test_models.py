from django.test import TestCase

from core import models


class ModelTests(TestCase):

    def test_disease_classification_str(self):
        """Test ICD Classification String Representation"""
        classification = models.DiseaseClassification.objects.create(
            classification_standard='icd-10',
            category_code='A0',
            diagnosis_code='1234',
            full_code='A01234',
            abbreviated_description='Comma-ind anal ret',
            full_description='Comma-induced anal retention',
            category_title='Malignant neoplasm of anus and anal canal'
        )

        self.assertEqual(str(classification), classification.full_code)
