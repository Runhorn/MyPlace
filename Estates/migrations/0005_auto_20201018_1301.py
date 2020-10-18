# Generated by Django 3.0.6 on 2020-10-18 11:01

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('Estates', '0004_auto_20201016_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estate',
            name='main_photo',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=75, size=[480, 240], upload_to='media/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='estate',
            name='photo_1',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, quality=75, size=[480, 240], upload_to='media/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='estate',
            name='photo_2',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, quality=75, size=[480, 240], upload_to='media/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='estate',
            name='photo_3',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, quality=75, size=[480, 240], upload_to='media/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='estate',
            name='photo_4',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, quality=75, size=[480, 240], upload_to='media/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='estate',
            name='photo_5',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, quality=75, size=[480, 240], upload_to='media/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='estate',
            name='photo_6',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, quality=75, size=[480, 240], upload_to='media/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='estate',
            name='type_of_building',
            field=models.IntegerField(choices=[(1, 'Mieszkanie'), (2, 'Apartament'), (3, 'Szeregówka'), (4, 'Dom'), (5, 'Loft'), (6, 'Inne')], default='INNE'),
        ),
    ]
