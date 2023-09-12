from django import forms

from car_collection.car.models import Car


class CreateCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

class ShowCarCatalogue(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('type', 'model', 'car_image',)