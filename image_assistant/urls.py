from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('home', views.home, name='home'),
    path('editing', views.editing, name='editing'),
    path('ocr', views.maincontent, name='ocr'),
    path('annotation', views.annotation, name='annotation'),
    path('similar', views.similar, name='similar'),
]