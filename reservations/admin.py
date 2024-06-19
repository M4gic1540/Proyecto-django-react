from django.contrib import admin
from .models import User, Room, Reservation
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(Room)
admin.site.register(Reservation)