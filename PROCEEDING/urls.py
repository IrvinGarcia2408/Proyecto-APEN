from django.urls import path
from PROCEEDING import views

urlpatterns = [
    path('', views.show_proceedings, name="show_proceedings"),
    path('list_proceedings/', views.list_proceedings, name="list_proceedings"),
    path('crear/', views.create_proceeding, name="create_proceeding"),
    path('crear/estados/', views.get_states, name="get_states"),
    path('crear/municipios/', views.get_municipalities, name="get_municipalities"),
    path('editar/<int:proceeding_id>', views.update_proceeding, name="update_proceeding"),
    path('eliminar', views.delete_proceeding, name="delete_proceeding")
]   