from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page

from car_collection.account.models import Profile



@cache_page(15 * 60)
def index(request):
    cars = CarLookedAt.objects.all()

    context = {
        'cars': cars,
    }

    return render(request, 'common/index.html', context)
