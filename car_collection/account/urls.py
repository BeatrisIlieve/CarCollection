from django.urls import path

from car_collection.account.views import create_profile, delete_profile, details_profile, edit_profile

urlpatterns = (
    path('create/', create_profile, name='create profile'),
    path('delete/', delete_profile, name='delete profile'),
    path('details/', details_profile, name='details profile'),
    path('edit/', edit_profile, name='edit profile')
)