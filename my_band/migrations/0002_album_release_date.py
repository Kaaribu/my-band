# Generated by Django 4.1.4 on 2023-01-09 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_band', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='release_date',
            field=models.DateField(null=True),
        ),
    ]
