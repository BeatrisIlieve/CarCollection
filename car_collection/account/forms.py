import os

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


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()

    def save(self, commit=True):
        profile_image_path = self.instance.profile_image.path

        if commit:
            self.instance.delete()
            os.remove(profile_image_path)

        return self.instance
