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
        fields = '__all__'

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        else:
            pass
        return self.instance


class EditCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
