from datetime import datetime
from django.db import models
from Owner.models import Owner
from django_resized import ResizedImageField

class Estate(models.Model):
    Types_of_building = [(1, ('Mieszkanie')),
                         (2, ('Apartament')),
                         (3, ('Szeregówka')),
                         (4, ('Dom')),
                         (5, ('Loft')),
                         (6, ('Inne'))]

    Materials_of_building = [(1, ('CEGŁA')),
                             (2, ('DREWNO')),
                             (3, ('WIELKA PŁYTA')),
                             (4, ('PUSTAK')),
                             (5, ('BETON')),
                             (6, ('ŻELBET')),
                             (6, ('INNE'))
                             ]

    owner = models.ForeignKey(Owner, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    surface = models.CharField(max_length=8)
    type_of_building = models.IntegerField(choices=Types_of_building, default='INNE')
    material_of_building = models.IntegerField(choices=Materials_of_building, default='INNE')
    year_of_building = models.IntegerField(default='2020')
    number_of_rooms = models.IntegerField()
    number_of_bathrooms = models.IntegerField()
    number_of_floors = models.IntegerField()
    max_floor = models.IntegerField()
    free_from = models.DateTimeField(blank=True)
    garage = models.BooleanField(default=False)
    parking_slot = models.BooleanField(default=False)
    price = models.CharField(max_length=6)
    city = models.CharField(max_length=15)
    street = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    main_photo = ResizedImageField(upload_to='media/%Y/%m/%d', size = [480,240])
    photo_1 = ResizedImageField(upload_to='media/%Y/%m/%d', size = [480,240], blank=True)
    photo_2 = ResizedImageField(upload_to='media/%Y/%m/%d', size = [480,240], blank=True)
    photo_3 = ResizedImageField(upload_to='media/%Y/%m/%d', size = [480,240], blank=True)
    photo_4 = ResizedImageField(upload_to='media/%Y/%m/%d', size = [480,240], blank=True)
    photo_5 = ResizedImageField(upload_to='media/%Y/%m/%d', size = [480,240], blank=True)
    photo_6 = ResizedImageField(upload_to='media/%Y/%m/%d', size = [480,240], blank=True)
    published = models.DateTimeField(default=datetime.now)
    reserved = models.BooleanField(default=False)

    def __str__(self):
        return self.title
