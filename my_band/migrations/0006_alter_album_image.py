# Generated by Django 4.1.4 on 2023-01-10 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_band', '0005_album_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='image',
            field=models.ImageField(null=True, upload_to='img/alb-art'),
        ),
    ]
