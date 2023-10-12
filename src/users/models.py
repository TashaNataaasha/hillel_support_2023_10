from django.db import models

class User(models.Model):
    email = models.EmailField(max_length=40)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.ForeignKey()
    
class Role(models.Model):
    value = models.CharField(max_length=15)
    
    
class Issue(models.Model):
    title = models.CharField(max_length=55)
    body = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    junior = models.IntegerField()
    senior = models.IntegerField(null=True)
    status = models.CharField(max_length=10)

class Message(models.Model):
    body = models.CharField(max_length=255)
    issue = models.IntegerField()
    user = models.IntegerField(null=True)