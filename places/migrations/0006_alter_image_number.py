# Generated by Django 4.0.3 on 2022-03-23 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_alter_place_description_long_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='number',
            field=models.IntegerField(blank=True, verbose_name='Номер'),
        ),
    ]
