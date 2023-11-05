from django.db import models
from users.constants import Role

class Issue(models.Model):
    # Your Issue model fields, including relationships with users (senior and junior)
    senior = models.ForeignKey('YourUserModel', on_delete=models.CASCADE, related_name='senior_issues')
    junior = models.ForeignKey('YourUserModel', on_delete=models.CASCADE, related_name='junior_issues')

class Message(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    author = models.ForeignKey('YourUserModel', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)