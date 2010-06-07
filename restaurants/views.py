from django.shortcuts import render_to_response
from django.template import RequestContext
from restaurants.filters import RestaurantFilter
from restaurants.models import Restaurant

def restaurant_list(request):
    """
    Restaurant list searchable by cuisine 
    choice, a text query, or both.
    """
    f = RestaurantFilter(request.GET, queryset=Restaurant.objects.all())
    return render_to_response("restaurants/restaurant_list.html", {
            "filter": f,
    }, context_instance=RequestContext(request))
