from django.urls import path
from DOCUMENTATION import views

urlpatterns = [
    path('', views.documentation, name="documentation"),
]   