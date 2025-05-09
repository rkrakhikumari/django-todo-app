from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ADMIN = 'admin'
    MANAGER = 'manager'
    USER = 'user'
    
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (MANAGER, 'Manager'),
        (USER, 'User'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=USER)
    
    def is_admin(self):
        return self.role == self.ADMIN
    
    def is_manager(self):
        return self.role == self.MANAGER
    
    def is_regular_user(self):
        return self.role == self.USER

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tasks')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks', null=True, blank=True)
    
    def __str__(self):
        return self.title
