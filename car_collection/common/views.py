from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page

from car_collection.account.models import Profile


# def get_profile():
#     try:
#         return Profile.objects.get()
#     except Profile.DoesNotExist as ex:
#         return None
#
#
# def index(request):
#     profile = get_profile()
#
#     if profile is None:
#         return render(request, 'common/index.html')
#     return render(request, 'common/index.html')

@cache_page(15 * 60)
def index(request):
    return render(request, 'common/index.html')
