from django import forms
from .models import User


class UserLogin(forms.ModelForm):
    class Meta:
        model = User
        fields = "username", "password"
