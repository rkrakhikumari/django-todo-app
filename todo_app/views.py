from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.messages.views import SuccessMessageMixin
from .models import User, Task
from .forms import CustomUserCreationForm, UserRoleUpdateForm, TaskForm, CustomPasswordResetForm, CustomSetPasswordForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.views import View
from .models import Task




class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "You have been logged out.")
        return redirect('login')

# Role-based access mixins
class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin()

class ManagerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_admin() or self.request.user.is_manager())

# User Views
class RegisterView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'todo_app/register.html'
    success_url = reverse_lazy('login')

class UserListView(AdminRequiredMixin, ListView):
    model = User
    template_name = 'todo_app/user_list.html'
    context_object_name = 'users'

class UserUpdateView(AdminRequiredMixin, UpdateView):
    model = User
    form_class = UserRoleUpdateForm
    template_name = 'todo_app/user_form.html'
    success_url = reverse_lazy('user-list')

# Task Views
class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'todo_app/task_list.html'
    context_object_name = 'tasks'
    
    

class TaskCreateView(ManagerRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'todo_app/task_form.html'
    success_url = reverse_lazy('task-list')
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class TaskUpdateView(ManagerRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'todo_app/task_form.html'
    success_url = reverse_lazy('task-list')

class TaskDeleteView(ManagerRequiredMixin, DeleteView):
    model = Task
    template_name = 'todo_app/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')

# Password Reset Views
class CustomPasswordResetView(SuccessMessageMixin, PasswordResetView):
    template_name = 'todo_app/password_reset_form.html'
    email_template_name = 'todo_app/password_reset_email.html'
    form_class = CustomPasswordResetForm
    success_url = reverse_lazy('password_reset_done')
    success_message = "An email with instructions to reset your password has been sent."

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'todo_app/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'todo_app/password_reset_confirm.html'
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy('password_reset_complete')

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'todo_app/password_reset_complete.html'
