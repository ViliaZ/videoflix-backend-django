from django.db import models
from django.db.models import FileField

class Movie (models.Model):
    title =  models.CharField(max_length=100)
    description = models.TextField()
    file = FileField(upload_to="", blank=True, null=True)                     

    def __str__(self):
        return self.title