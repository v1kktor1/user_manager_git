from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.ForeignKey('Role', on_delete=models.CASCADE, related_name='users')

class Role(models.Model):
    name = models.CharField(max_length=50, choices=[('admin', 'Admin'), ('user', 'User')])