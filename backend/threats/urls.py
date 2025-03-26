from django.urls import path
from . import views

urlpatterns = [
    path('top-countries/', views.top_countries),
    path('top-years/', views.top_years),
    path('top-threat-types/', views.top_threat_types),
    path('top-industries/', views.top_industries),
]
