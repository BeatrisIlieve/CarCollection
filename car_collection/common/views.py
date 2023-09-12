from django.shortcuts import render, redirect

from car_collection.account.models import Profile


def get_profile():
    try:
        return Profile.objects.get()
    except:
        return None

def index(request):

    profile = get_profile()

    if profile is None:
       return render(request, 'common/index_without_profile.html')
    return render(request, 'common/index_with_profile.html')
