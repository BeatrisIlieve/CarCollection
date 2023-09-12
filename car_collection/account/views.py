from django.shortcuts import render, redirect

from car_collection.account.forms import CreateProfileForm, EditProfileForm
from car_collection.common.views import get_profile


def create_profile(request):

    if request.method == 'GET':
        form = CreateProfileForm()

    else:
        form = CreateProfileForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
    }

    return render(request, 'account/profile-create.html', context)


def delete_profile(request, pk):
    return render(request, 'account/profile-delete.html')


def details_profile(request, pk):
    return render(request, 'account/profile-details.html')


def edit_profile(request, pk):

    profile = get_profile()

    if request.method == 'GET':
        form = EditProfileForm(instance=profile)

    else:
        form = EditProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
    }

    return render(request, 'account/profile-edit.html', context)