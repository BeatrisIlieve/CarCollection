from django.urls import path, include

from car_collection.car.views import create_car, delete_car, details_car, edit_car, show_catalogue

urlpatterns = (
    path('catalogue/', show_catalogue, name='catalogue'),
    path('create/', create_car, name='create car'),
    path('<int:pk>/', include(
        [
            path('details/', details_car, name='details car'),
            path('edit/', edit_car, name='edit car'),
            path('delete/', delete_car, name='delete car'),
        ]
    )),
)
