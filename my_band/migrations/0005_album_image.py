# Generated by Django 4.1.4 on 2023-01-10 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_band', '0004_album_price_alter_customer_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='image',
            field=models.ImageField(null=True, upload_to='static/img/alb-art'),
        ),
    ]
