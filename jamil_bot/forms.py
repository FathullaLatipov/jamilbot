from django import forms

from jamil_bot.models import VehicleModel


class VehicleModelForm(forms.ModelForm):
    class Meta:
        model = VehicleModel
        fields = ['name', 'color', 'year']
