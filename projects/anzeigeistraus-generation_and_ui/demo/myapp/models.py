from django.db import models
from django.utils import timezone

# Create your models here.
class ChatHistory(models.Model):
    query = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Query: {self.query} - Response: {self.response} - Timestamp: {self.timestamp}"
