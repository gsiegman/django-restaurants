from django.contrib import admin
from restaurants.models import Restaurant, RestaurantCuisineType

admin.site.register(Restaurant)
admin.site.register(RestaurantCuisineType)
