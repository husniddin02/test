# Generated by Django 5.0.2 on 2024-03-13 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_news_options_alter_news_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='details_link',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на подробности'),
        ),
    ]
