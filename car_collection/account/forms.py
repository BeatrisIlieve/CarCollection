import os

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UsernameField

from car_collection.account.models import Profile


CarCollectionUserModel = get_user_model()

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = CarCollectionUserModel
        fields = (CarCollectionUserModel.USERNAME_FIELD,)
        field_classes = {
            'username': UsernameField,
        }

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = Profile(
            user=user,
        )

        if commit:
            profile.save()

        return user

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'age', 'profile_image',)
        field_classes = {
            'username': UsernameField,
        }


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
