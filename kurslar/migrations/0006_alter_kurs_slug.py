# Generated by Django 4.2.3 on 2023-07-27 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kurslar', '0005_remove_kurs_kategori_kurs_kategori'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kurs',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
