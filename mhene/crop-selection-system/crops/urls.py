from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/<str:region>/', views.dashboard_by_region, name='dashboard_by_region'),
    path('crops/<str:region>/', views.crops_by_region, name='crops_by_region'),
]