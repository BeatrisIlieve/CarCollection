from django.contrib import admin

from car_collection.account.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
