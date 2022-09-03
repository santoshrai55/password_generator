from . import views
from django.urls import path
app_name = 'generator_app'

urlpatterns = [
    path('', views.home, name='home')
]
