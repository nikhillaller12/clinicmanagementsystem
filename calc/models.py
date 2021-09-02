from django.db import models

# Create your models here.

class medicalrecords(models.Model):
        name=models.CharField(max_length=100)
        gender=models.CharField(max_length=50)
        martial=models.CharField(max_length=50)
        number=models.BigIntegerField()
        dateofbirth=models.DateField()
        address=models.TextField()
        city=models.CharField(max_length=100)
        state=models.CharField(max_length=100)
        pincode=models.IntegerField()
        disease=models.TextField()
        medicine=models.CharField(max_length=50)
        allergies=models.CharField(max_length=50)
        tobacco=models.CharField(max_length=50)
        drugs=models.CharField(max_length=50)
        alchohol=models.CharField(max_length=50)
        generalhealth=models.IntegerField()


