from django.contrib import admin
from .models import Reservation, Guest, Movie
# Register your models here.

admin.site.register(Reservation)
admin.site.register(Guest)
admin.site.register(Movie)