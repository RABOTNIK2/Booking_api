from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

class Hotel(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    image = models.TextField()
    rating = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(10)])
    adress = models.TextField()
    contacts = models.CharField(max_length=50)
    amenities = models.TextField()
    is_animals = models.BooleanField()
    single_room = models.PositiveIntegerField(null=True)
    double_room = models.PositiveIntegerField(null=True)
    multi_room = models.PositiveIntegerField(null=True)
    price_per_night = models.PositiveIntegerField(null = False)
    
    def __str__(self):
        return self.name


class User(AbstractUser):
    phone = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999), MinValueValidator(1000000000)])
    favorite = models.ManyToManyField(Hotel, blank=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']
    
    def __str__(self):
        return self.username
    
class Booking(models.Model):
    user_booking = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    arrival_date = models.DateField()
    date_of_dispatch = models.DateField()
    quantity_single_room = models.PositiveIntegerField(null=False)
    quantity_double_room = models.PositiveIntegerField(null=True)
    quantity_multi_room = models.PositiveIntegerField(null=True)
    
class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel_review = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.TextField(null=True, blank=True)
    reaction = models.PositiveIntegerField(validators=[MaxValueValidator(10)])
    posted_at = models.DateTimeField(default=datetime.datetime.now)

# Create your models here.
