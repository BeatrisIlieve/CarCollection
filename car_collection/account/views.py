from django.shortcuts import render


def create_profile(request):
    return render(request, 'account/profile-create.html')


def delete_profile(request, pk):
    return render(request, 'account/profile-delete.html')


def details_profile(request, pk):
    return render(request, 'account/profile-details.html')


def edit_profile(request, pk):
    return render(request, 'account/profile-edit.html')