"""ProyectoAPEN URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('LOGIN.urls')),
    path('banfe/', include('BANFE.urls')),
    path('expedientes/', include('PROCEEDING.urls')),
    path('pruebas/', include('TEST_HISTORY.urls')),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='recover_password/password_reset_form.html', email_template_name='recover_password/password_reset_email.html'),name='password_reset'),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(template_name='recover_password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='recover_password/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='recover_password/password_reset_complete.html'), name='password_reset_complete'),
]

urlpatterns += staticfiles_urlpatterns()