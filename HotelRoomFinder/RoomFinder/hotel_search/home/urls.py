from django.urls import path
from .views import home, get_hotel

urlpatterns = [
    path('', home),  # This should render the home page
    path('api/get_GFG/', get_hotel),  # API endpoint for hotel data
]

