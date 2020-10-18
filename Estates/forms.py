from django import forms
from . import models


class CreateEstateOffer(forms.ModelForm):
    class Meta:
        model = models.Estate

