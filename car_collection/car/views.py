from django.shortcuts import render, redirect

from car_collection.car.forms import CreateCarForm


def create_car(request):

    if request.method == 'GET':
        form = CreateCarForm()

    else:
        form = CreateCarForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
    }

    return render(request, 'car/car-create.html', context)


def delete_car(request, pk):
    return render(request, 'car/car-delete.html')


def details_car(request, pk):
    return render(request, 'car/car-details.html')


def edit_car(request, pk):
    return render(request, 'car/car-edit.html')


def show_catalogue(request):
    return render(request, 'car/catalogue.html')