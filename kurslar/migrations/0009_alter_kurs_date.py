# Generated by Django 4.2.3 on 2023-07-28 06:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kurslar', '0008_alter_kurs_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kurs',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 7, 28, 9, 56, 43, 852619)),
        ),
    ]
