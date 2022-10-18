from django.urls import path
from .views import index, filter

urlpatterns = [
    path('', index, name="index"),
    path('filter/', filter, name="filter"),
]
