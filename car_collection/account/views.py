from django.shortcuts import render, redirect

from car_collection.account.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
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
    profile = get_profile()

    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)

    else:
        form = DeleteProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
        'profile': profile,
        'pk': pk,
    }

    return render(request, 'account/profile-delete.html', context)


def details_profile(request, pk):
    profile = get_profile()

    context = {
        'profile': profile,
        'pk': pk,
    }

    return render(request, 'account/profile-details.html', context)


def edit_profile(request, pk):
    profile = get_profile()

    if request.method == 'GET':
        form = EditProfileForm(instance=profile)

    else:
        form = EditProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('details profile', pk=profile.pk)

    context = {
        'form': form,
        'profile': profile,
        'pk': pk,
    }

    return render(request, 'account/profile-edit.html', context)
