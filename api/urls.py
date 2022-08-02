from django.urls import path
from api.views import RainfallDrainApi

app_name = 'api'

urlpatterns = [
    path('rainfall-drain/', RainfallDrainApi.as_view(), name='rainfall-drain')
]