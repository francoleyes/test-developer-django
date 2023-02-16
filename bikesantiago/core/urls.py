from django.urls import path
from . import views

urlpatterns = [
    path('bikesantiago/', views.bike_santiago_view, name="bikesantiago"),
    path('', views.projects_view, name="projects"),
]