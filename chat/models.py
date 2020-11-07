from django.db import models


class Dialog(models.Model):
    dialogmans = models.CharField(max_length=50, unique=True)
    message = models.TextField()

    def __str__(self):
        return self.message
# Create your models here. 
