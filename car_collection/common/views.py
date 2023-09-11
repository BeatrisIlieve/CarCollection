from django.shortcuts import render, redirect


def get_profile():
    return 'profile'

def index(request):
    profile = get_profile()
    if not profile:
       return render(request, 'common/index_without_profile.html')
    return render(request, 'common/index_with_profile.html')
