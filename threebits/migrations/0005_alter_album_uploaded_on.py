# Generated by Django 4.1.6 on 2023-04-08 01:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threebits', '0004_alter_album_uploaded_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='uploaded_on',
            field=models.DateField(default=datetime.datetime(2023, 4, 8, 1, 1, 12, 970896)),
        ),
    ]
