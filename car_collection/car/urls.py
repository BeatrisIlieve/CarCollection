from django.urls import path

from car_collection.car.views import create_car, delete_car, details_car, edit_car, show_catalogue

urlpatterns = (
    path('create/', create_car, name='create car'),
    path('delete/<int:pk>/', delete_car, name='delete car'),
    path('details/<int:pk>/', details_car, name='details car'),
    path('edit/<int:pk>/', edit_car, name='edit car'),
    path('catalogue/', show_catalogue, name='catalogue'),
)