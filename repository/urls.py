from django.urls import path

from . import views

urlpatterns = [
    path('course/<slug:slug>/', views.course_detail, name='course_detail'),
    path('courses/', views.courses, name='courses'),
    path('level/<slug:slug>/', views.level, name='level'),
    path('materials/', views.materials, name='materials'),
    path('materials/<slug:slug>/', views.course_material, name='course_material'),
    path('search/', views.search, name='search'),
    path('', views.home, name='home'),
]
