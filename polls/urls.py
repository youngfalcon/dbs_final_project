from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customer-registration/', views.customerRegistration, name='customer-registration'),
    path('assessment-entry/', views.assessmentEntry, name='assessment-entry'),
    path('quote-retrieval/', views.quoteRetrieval, name='quote-retrieval'),
    path('updateGeneralModel/', views.updateGeneralModel, name='updateGeneralModel'),
    path('updateHeartModel/', views.updateHeartModel, name='updateHeartModel'),
    path('updateStrokeModel/', views.updateStrokeModel, name='updateStrokeModel'),
]