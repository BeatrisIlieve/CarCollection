import os

from django import forms

from car_collection.car.models import Car


class CreateCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class ShowCarCatalogue(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('brand', 'model', 'car_image',)


class DeleteCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ()

    def save(self, commit=True):
        car_image_path = self.instance.car_image.path

        if commit:
            self.instance.delete()
            os.remove(car_image_path)

        return self.instance


class EditCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
