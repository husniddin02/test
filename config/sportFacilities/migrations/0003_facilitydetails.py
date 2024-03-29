# Generated by Django 5.0.2 on 2024-03-13 01:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportFacilities', '0002_alter_sportsfacility_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacilityDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details_link', models.URLField(verbose_name='Ссылка на дополнительные данные')),
                ('facility', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='sportFacilities.sportsfacility', verbose_name='Спортивный объект')),
            ],
            options={
                'verbose_name': 'Подробности спортивного объекта',
                'verbose_name_plural': 'Подробности спортивных объектов',
            },
        ),
    ]
