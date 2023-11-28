from django.urls import path

from sveta_rest.views import get_api_page

urlpatterns = [
    path('rest/', get_api_page),
]