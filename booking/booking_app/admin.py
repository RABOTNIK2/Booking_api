from django.contrib import admin
from .models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name']

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'description']
    
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user_booking', 'hotel', 'arrival_date']
    
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['author', 'content', 'reaction']  
    
# Register your models here.
