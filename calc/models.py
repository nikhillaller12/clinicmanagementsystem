from django.db import models

# Create your models here.

class registery(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    doctor = models.BooleanField(default=False)

    def __str__(self):
        return self.title