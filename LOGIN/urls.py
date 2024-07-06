from django.urls import path
from LOGIN import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('apen/', views.inicio, name="inicio"),
    path('login/', views.login, name = "login"),
    path('registro/', views.register, name="register"),
    path('logout/', views.logout_user, name="logout"),
] 