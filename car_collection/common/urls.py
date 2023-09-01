from django.urls import path

from car_collection.common.views import index

urlpatterns = (
    path('', index, name='home page'),
)