from django.db import models
from venues.models import Venue

CUISINE_CHOICES = (
    ('american', 'American'),
    ('argentine', 'Argentine'),
    ('asian', 'Asian'),
    ('bbq', 'Barbeque'),
    ('cajun', 'Cajun/Creole'),
    ('caribbean', 'Caribbean'),
    ('chinese', 'Chinese'),
    ('cuban', 'Cuban'),
    ('deli', 'Deli'),
    ('ethiopian', 'Ethiopian'),
    ('fast', 'Fast Food'),
    ('fine', 'Fine Dining'),
    ('french', 'French'),
    ('german', 'German'),
    ('greek', 'Greek'),
    ('hotdog', 'Hot Dogs'),
    ('hungarian', 'Hungarian'),
    ('indian', 'Indian'),
    ('indonesian', 'Indonesian'),
    ('italian', 'Italian'),
    ('japanese', 'Japanese'),
    ('korean', 'Korean'),
    ('kosher', 'Kosher'),
    ('mexican', 'Mexican'),
    ('pizza', 'Pizza'),
    ('seafood', 'Seafood'),
    ('southern', 'Southern'),
    ('steak', 'Steak'),
    ('sushi', 'Sushi Bar'),
    ('texmex', 'Tex-Mex'),
    ('thai', 'Thai'),
    ('vegan', 'Vegan'),
    ('vietnam', 'Vietnamese'),
)

class Restaurant(Venue):
    cuisine = models.CharField(max_length=50, choices=CUISINE_CHOICES)
    price_range = models.CharField(max_length=25, blank=True)
    delivery = models.NullBooleanField()
    buffet = models.NullBooleanField()
    outdoor_seating = models.NullBooleanField()
    party_room = models.NullBooleanField()
    accepts_reservations = models.NullBooleanField()
    has_carryouts = models.NullBooleanField()
    has_kids_menu = models.NullBooleanField()
    has_wifi = models.NullBooleanField()
