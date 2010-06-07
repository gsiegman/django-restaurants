from django.core.urlresolvers import reverse
from django.db import models
from venues.models import Venue

class RestaurantCuisineType(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Restaurant(Venue):
    cuisine = models.ForeignKey(RestaurantCuisineType)
    price_range = models.CharField(max_length=25, blank=True)
    delivery = models.NullBooleanField()
    buffet = models.NullBooleanField()
    outdoor_seating = models.NullBooleanField()
    party_room = models.NullBooleanField()
    accepts_reservations = models.NullBooleanField()
    has_carryouts = models.NullBooleanField()
    has_kids_menu = models.NullBooleanField()
    has_wifi = models.NullBooleanField()

    def save(self, *args, **kwargs):
        self.venue_model_type = 'restaurants.restaurant'
        super(Restaurant, self).save(*args, **kwargs)
