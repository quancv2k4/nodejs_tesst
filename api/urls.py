from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListCreateView.as_view(), name='users-list'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='users-detail'),
    path('health/', views.health_check, name='health-check'),
]
