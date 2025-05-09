from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    # Authentication URLs
    path('login/', LoginView.as_view(template_name='todo_app/login.html'), name='login'),
    # path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    
    # Password Reset URLs
    path('password-reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    # User Management URLs
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/update/', views.UserUpdateView.as_view(), name='user-update'),
    
    # Task URLs
    path('', views.TaskListView.as_view(), name='task-list'),
    path('tasks/create/', views.TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/update/', views.TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task-delete'),
]