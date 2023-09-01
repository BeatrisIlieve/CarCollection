from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('car_collection.common.urls')),
    path('account/', include('car_collection.account.urls')),
    path('car/', include('car_collection.car.urls')),
]
