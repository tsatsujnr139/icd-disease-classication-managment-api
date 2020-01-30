from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import DiseaseClassification
from disease_classification.serializers import DiseaseClassificationSerializer


DISEASE_CLASSIFICATION_URL = reverse(
    'disease_classification:diseaseclassification-list')


def get_detail_url(disease_id):
    """return disease_classification detail URL"""
    return reverse(
        'disease_classification:diseaseclassification-detail',
        kwargs={
            'id': disease_id})


def sample_disease_classification(**params):
    """Tests for disease_classification API"""

    defaults = {
        'classification_standard': 'icd-10',
        'category_code': 'A0',
        'diagnosis_code': '1234',
        'full_code': 'A01234',
        'abbreviated_description': 'Comma-ind anal ret',
        'full_description': 'Comma-induced anal retention',
        'category_title': 'Malignant neoplasm of anus and anal canal'
    }

    defaults.update(params)

    return DiseaseClassification.objects.create(
        **defaults
    )


class DiseaseClassificationTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_classifications_succssfully(self):
        """Test that disease classifications are retrieved successfully"""

        sample_disease_classification()
        sample_disease_classification(
            category_code='C00', full_code='C001234')

        res = self.client.get(DISEASE_CLASSIFICATION_URL)
        disease_classifications = DiseaseClassification.objects.all().order_by(
            'id')

        serializer = DiseaseClassificationSerializer(
            disease_classifications, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['count'], 2)
        self.assertTrue(len(res.data['results']) <= 20)
        self.assertEqual(res.data['results'], serializer.data)

    def test_retrieve_20_classfications_max_per_page(self):
        """
        Test that disease classifications are
        retrieved in batches of 20 per page
        """

        sample_disease_classification()
        sample_disease_classification(
            category_code='C00', full_code='C001234')
        sample_disease_classification(
            category_code='D00', full_code='D001234')
        sample_disease_classification(
            category_code='E00', full_code='E001234')
        sample_disease_classification(
            category_code='F00', full_code='F001234')
        sample_disease_classification(
            category_code='G00', full_code='G001234')
        sample_disease_classification(
            category_code='H00', full_code='H001234')
        sample_disease_classification(
            category_code='I00', full_code='I001234')
        sample_disease_classification(
            category_code='J00', full_code='J001234')
        sample_disease_classification(
            category_code='K00', full_code='K001234')
        sample_disease_classification(
            category_code='L00', full_code='L001234')
        sample_disease_classification(
            category_code='M00', full_code='M001234')
        sample_disease_classification(
            category_code='N00', full_code='N001234')
        sample_disease_classification(
            category_code='O00', full_code='O001234')
        sample_disease_classification(
            category_code='P00', full_code='P001234')
        sample_disease_classification(
            category_code='Q00', full_code='Q001234')
        sample_disease_classification(
            category_code='R00', full_code='R001234')
        sample_disease_classification(
            category_code='S00', full_code='S001234')
        sample_disease_classification(
            category_code='T00', full_code='T001234')
        sample_disease_classification(
            category_code='U00', full_code='U001234')
        sample_disease_classification(
            category_code='V00', full_code='V001234')
        sample_disease_classification(
            category_code='W00', full_code='W001234')

        res = self.client.get(DISEASE_CLASSIFICATION_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['count'], 22)
        self.assertTrue(len(res.data['results']) <= 20)

    def test_add_disease_classification(self):
        """ Test add new classification successfully"""

        payload = {
            'classification_standard': 'icd-10',
            'category_code': 'A0',
            'diagnosis_code': '1234',
            'full_code': 'A01234',
            'abbreviated_description': 'Comma-ind anal ret',
            'full_description': 'Comma-induced anal retention',
            'category_title': 'Malignant neoplasm of anus and anal canal'}

        res = self.client.post(DISEASE_CLASSIFICATION_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        disease_classification_created = DiseaseClassification.objects.filter(
            full_code='A01234').exists
        self.assertTrue(disease_classification_created)

    def test_add_disease_classification_invalid_payload(self):
        """ Test add new classification with invalid payload fails"""
        res = self.client.post(DISEASE_CLASSIFICATION_URL, {})
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_disease_classification(self):
        """ Test Update a Disease Classification"""

        disease = sample_disease_classification()

        payload = {
            'diagnosis_code': '6789',
            'full_code': 'A06789'
        }

        url = get_detail_url(disease.id)
        self.client.patch(url, payload)
        disease.refresh_from_db()
        self.assertEqual(disease.full_code, payload['full_code'])

    def test_delete_disease_classification(self):
        """Test Deletion of a Disease Classification"""

        disease = sample_disease_classification()
        url = get_detail_url(disease.id)
        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
