from django.db import models

# Create your models here.
class book_appointment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phno = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()