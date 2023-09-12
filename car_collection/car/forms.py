from django import forms

from car_collection.car.models import Car


class CreateCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'