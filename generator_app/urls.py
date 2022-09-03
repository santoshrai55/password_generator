from . import views
from django.urls import path
name = 'generator_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('generated_password', views.password, name='password')
]
