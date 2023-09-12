from django.shortcuts import render, redirect

from car_collection.car.forms import CreateCarForm, DeleteCarForm
from car_collection.car.models import Car


def create_car(request):

    if request.method == 'GET':
        form = CreateCarForm()

    else:
        form = CreateCarForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'car/car-create.html', context)


def delete_car(request, pk):

    car = Car.objects.all().filter(pk=pk).get()

    if request.method == 'GET':
        form = DeleteCarForm(instance=car)

    else:
        form = DeleteCarForm(request.POST, request.FILES, instance=car)

        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'car': car,
        'pk': pk,
    }

    return render(request, 'car/car-delete.html', context)


def details_car(request, pk):

    car = Car.objects.all().filter(pk=pk).get()

    context = {
        'car': car,
        'pk': pk,
    }

    return render(request, 'car/car-details.html', context)


def edit_car(request, pk):
    return render(request, 'car/car-edit.html')


def show_catalogue(request):
    context = {
        'cars': Car.objects.all()
    }

    return render(request, 'car/catalogue.html', context)