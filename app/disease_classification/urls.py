from django.urls import path, include

from disease_classification import views

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('diagnosis',
                views.DiseaseClassificationViewSet,
                basename='diseaseclassification')

app_name = 'disease_classification'

urlpatterns = [
    path('', include(router.urls))
]
