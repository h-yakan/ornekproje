# Generated by Django 4.2.3 on 2023-07-27 08:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kurslar', '0007_alter_kurs_kategori'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kurs',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 7, 27, 8, 25, 41, 138658, tzinfo=datetime.timezone.utc)),
        ),
    ]
