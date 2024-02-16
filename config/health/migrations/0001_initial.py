# Generated by Django 5.0.1 on 2024-02-16 14:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0003_user_delete_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Health',
            fields=[
                ('health_id', models.AutoField(primary_key=True, serialize=False)),
                ('height', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('heart_rate', models.IntegerField(blank=True, null=True)),
                ('bmi', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('bmi_category', models.CharField(blank=True, max_length=50, null=True)),
                ('additional_notes', models.TextField(blank=True, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]
