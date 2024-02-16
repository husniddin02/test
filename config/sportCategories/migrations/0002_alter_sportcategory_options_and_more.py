# Generated by Django 5.0.1 on 2024-02-16 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportCategories', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sportcategory',
            options={'verbose_name': 'Категория спорта', 'verbose_name_plural': 'Категории спорта'},
        ),
        migrations.AlterField(
            model_name='sportcategory',
            name='category_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Уникальный идентификатор категории спорта'),
        ),
        migrations.AlterField(
            model_name='sportcategory',
            name='category_name',
            field=models.CharField(max_length=100, verbose_name='Название категории спорта'),
        ),
        migrations.AlterField(
            model_name='sportcategory',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
    ]