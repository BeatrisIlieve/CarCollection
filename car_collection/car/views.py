from django.shortcuts import render


def create_car(request):
    return render(request, 'car/car-create.html')


def delete_car(request, pk):
    return render(request, 'car/car-delete.html')


def details_car(request, pk):
    return render(request, 'car/car-details.html')


def edit_car(request, pk):
    return render(request, 'car/car-edit.html')


def show_catalogue(request):
    return render(request, 'car/catalogue.html')