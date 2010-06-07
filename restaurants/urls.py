from django.conf.urls.defaults import *
from restaurants.models import Restaurant
from restaurants.views import restaurant_list

urlpatterns = patterns('',
    url(r'^$', 
        restaurant_list,
        name='restaurants_restaurant_index'
    )
)
