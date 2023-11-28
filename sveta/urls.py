from django.urls import path
from .views import get_index_page


urlpatterns = [
    path('django/', get_index_page),
]