from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('editing', views.editing, name='editing'),
    path('maincontent', views.maincontent, name='maincontent'),
    path('annotation', views.annotation, name='annotation'),
    path('similar', views.similar, name='similar'),
]