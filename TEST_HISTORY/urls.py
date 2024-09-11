from django.urls import path
from TEST_HISTORY import views

urlpatterns = [
    path('', views.show_tests, name="show_tests"),
    path('list_tests/', views.list_tests, name="list_tests"),
    path('details_banfe', views.details_banfe, name="details_banfe"),
    path('export-pdf/', views.export_table_pdf, name='export_table_pdf'),
    path('edit_banfe', views.edit_tests_banfe, name='edit_tests_banfe'),
    path('export_selected_tests_csv/', views.export_selected_tests_csv, name='export_selected_csv'),
]   