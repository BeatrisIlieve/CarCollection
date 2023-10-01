from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page

from car_collection.car.forms import CreateCarForm, DeleteCarForm, EditCarForm
from car_collection.car.models import Car


@cache_page(15 * 60)
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

@cache_page(15 * 60)
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

@cache_page(15 * 60)
def details_car(request, pk):
    car = Car.objects.all().filter(pk=pk).get()

    car_price = car.price

    context = {
        'car': car,
        'pk': pk,
        'car_price': car_price,
    }

    return render(request, 'car/car-details.html', context)


def edit_car(request, pk):
    car = Car.objects.all().filter(pk=pk).get()

    if request.method == 'GET':
        form = EditCarForm(instance=car)

    else:
        form = EditCarForm(request.POST, request.FILES, instance=car)

        if form.is_valid():
            form.save()
            return redirect('details car', pk=car.pk)

    context = {
        'form': form,
        'car': car,
        'pk': pk,
    }

    return render(request, 'car/car-edit.html', context)


def show_catalogue(request):
    total_cars = Car.objects.all().count()

    context = {
        'cars': Car.objects.all(),
        'total_cars': total_cars,
    }

    return render(request, 'car/catalogue.html', context)
