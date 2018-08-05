from django.contrib import admin
from django.urls import path, include

from posts import views

urlpatterns = [
    path('posts/', include('posts.urls')),
    path('admin/', admin.site.urls),
]
