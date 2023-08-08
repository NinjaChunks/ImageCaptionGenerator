from django.urls import path, include
from . import views

app_name = 'caption_generator'

urlpatterns = [
    path('', views.home, name='home'),
    path('generate_caption', views.process_image, name='generate_caption'),
    path('result/', views.result, name='result'),
]
