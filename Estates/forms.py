from django import forms
from . import models


class CreateEstateOffer(forms.ModelForm):
    class Meta:
        model = models.Estate
        fields = ['title',
                  'surface',
                  'type_of_building',
                  'material_of_building',
                  'year_of_building',
                  'number_of_rooms',
                  'number_of_bathrooms',
                  'number_of_floors',
                  'max_floor',
                  'free_from',
                  'garage',
                  'parking_slot',
                  'price',
                  'city',
                  'street',
                  'description',
                  'main_photo',
                  'photo_1',
                  'photo_2',
                  'photo_3',
                  'photo_4',
                  'photo_5',
                  'photo_6',
                  'published',
                  'reserved']
