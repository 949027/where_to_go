# Generated by Django 3.2.12 on 2022-02-25 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='imgs',
        ),
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.CharField(max_length=400, verbose_name='Краткое описание'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Номер')),
                ('file', models.ImageField(blank=True, upload_to='', verbose_name='Изображения')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.place', verbose_name='Место')),
            ],
        ),
    ]
