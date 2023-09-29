from django.contrib.auth import get_user_model, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from car_collection.account.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from car_collection.car.models import Car
from car_collection.common.views import get_profile

CarCollectionUserModel = get_user_model()


class SignUpView(CreateView):
    template_name = 'account/profile-create.html'
    form_class = CreateProfileForm
    success_url = reverse_lazy('home page', )

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result

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

    total_sum = sum(c.price for c in Car.objects.all())

    context = {
        'profile': profile,
        'pk': pk,
        'total_sum': total_sum,
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
