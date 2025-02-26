from django.db import models

# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('C', 'Completed'),
    ]
    
    name = models.CharField(max_length=225)
    description = models.TextField(blank=True, null=True)  # Optional field
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
