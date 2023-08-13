from django.db import models

# Create your models here.
class Contact(models.Model):
    email=models.CharField(max_length=110)
    contact=models.CharField(max_length=100)
    address=models.TextField()
    queries=models.TextField()
    #date=models.DateField()

    def __str__(self):
        return self.email