# Generated by Django 4.2.3 on 2023-08-02 14:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kurslar', '0015_alter_kurs_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kurs',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 8, 2, 17, 39, 43, 639577)),
        ),
    ]
