from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import FoydalanuvchiProfili


class RoyxatdanOtishForm(UserCreationForm):
    telefon_raqami = forms.IntegerField(label="Telefon raqami")

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            FoydalanuvchiProfili.objects.create(
                user=user,
                telefon_raqami=self.cleaned_data["telefon_raqami"],
            )
        return user
