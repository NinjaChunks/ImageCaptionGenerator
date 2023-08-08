from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('caption_generator.urls', namespace='caption_generator')),
]
