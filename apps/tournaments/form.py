from django import forms
from .models import Tournaments


class TournamentsForm(forms.ModelForm):
    class Meta:
        model = Tournaments
        fields = "__all__"
