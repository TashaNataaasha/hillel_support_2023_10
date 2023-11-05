from django.db import models

class Message(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)