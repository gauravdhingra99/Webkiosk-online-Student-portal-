from django.db import models

# Create your models here.
class User(models.Model):
    enroll=models.CharField(max_length=100)
    DOB=models.DateField()
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.enroll
