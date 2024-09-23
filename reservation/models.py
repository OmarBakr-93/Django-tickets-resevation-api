from django.db import models

# Create your models here.

class Guest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    hall = models.CharField(max_length=100)
    time = models.DateTimeField()
    movie = models.CharField(max_length=100)
    price = models.FloatField()
    
    def __str__(self):
        return self.movie

    
class Reservation(models.Model):
    guest = models.ForeignKey(Guest,related_name="reservations",on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,related_name="reservations",on_delete=models.CASCADE)
        