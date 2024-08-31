from django.db import models
from django.utils import timezone

class Student(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password1 = models.CharField(max_length=128)
    password2 = models.CharField(max_length=128)
    headline = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=50)
    about = models.TextField()
    skills = models.TextField()
    edu = models.TextField()
    additional = models.TextField()
    cv = models.IntegerField(default=10)

    def __str__(self):
        return self.username


class Alumni(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password1 = models.CharField(max_length=128)
    password2 = models.CharField(max_length=128)
    name = models.CharField(max_length=255, blank=True, null=True)
    headline = models.CharField(max_length=100)
    about = models.TextField()
    experience = models.CharField(max_length=100)
    additional = models.TextField()  # Consistent TextField with a default value

    def __str__(self):
        return self.username

# Notification model
class Notification(models.Model):
    recipient = models.ForeignKey(Alumni, on_delete=models.CASCADE, related_name='notifications')
    sender = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='sent_notifications')
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification from {self.sender.username} to {self.recipient.username}"
