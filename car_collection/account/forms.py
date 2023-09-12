from django import forms

from car_collection.account.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'