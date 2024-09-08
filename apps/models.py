from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone

from user_auth.models import User

class App(models.Model):
    PLATFORMS = [
        ('win', 'Windows'),
        ('mac', 'MacOS'),
        ('ios', 'iOS'),
        ('android', 'Android'),
        ('linux', 'Linux'),
    ]
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    version = models.CharField(max_length=200) # TODO: change to version
    platforms = ArrayField(models.CharField(max_length=100), blank=True, default=list)
    release_date = models.DateField()
    tags = ArrayField(models.CharField(max_length=200))
    price = models.FloatField(default=0)
    downloads = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    publish_datetime = models.DateTimeField(default=timezone.now)
    likes = ArrayField(models.CharField(max_length=200), default=list)
    
    def __str__(self):
        return f'{self.app.name} | {self.user.username} | {self.text}'