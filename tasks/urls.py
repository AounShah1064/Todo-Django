from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index.as_view(), name=''),
    path('update-task/<str:pk>/', views.updateTask.as_view(), name='update-task'),
    path('delete-task/<str:pk>/', views.deleteTask.as_view(), name='delete-task'),
    
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.RegisterView.as_view(), name='register'),
]