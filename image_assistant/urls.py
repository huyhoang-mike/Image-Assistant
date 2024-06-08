from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('editing/', views.editing, name='editing'),
    path('ocr/', views.maincontent, name='ocr'),
    path('annotation/', views.annotation, name='annotation'),
    path('similar/', views.similar, name='similar'),
    path('editing/result/', views.editing_r, name='editing_result'),
    path('ocr/result/', views.maincontent_r, name='ocr_result'),
    path('annotation/result/', views.annotation_r, name='annotation_result'),
    path('similar/result/', views.similar_r, name='similar_result'),
]