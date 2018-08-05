from django.contrib import admin
from django.conf.urls import  url,include
from django.urls import path

from posts import views

urlpatterns = [
    path('posts/', include('posts.urls')),
    path('admin/', admin.site.urls),
]
