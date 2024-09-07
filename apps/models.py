from django.db import models
from django.contrib.postgres.fields import ArrayField

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
    current_version = models.CharField(max_length=200) # TODO: change to version
    platforms = ArrayField(models.CharField(max_length=100), blank=True, default=list)
    release_date = models.DateField()
    tags = ArrayField(models.CharField(max_length=200))
    price = models.FloatField(default=0)
    downloads = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name