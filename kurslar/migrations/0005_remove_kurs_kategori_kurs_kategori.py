# Generated by Django 4.2.3 on 2023-07-27 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kurslar', '0004_alter_kurs_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kurs',
            name='kategori',
        ),
        migrations.AddField(
            model_name='kurs',
            name='kategori',
            field=models.ManyToManyField(blank=True, null=True, to='kurslar.kategoriler'),
        ),
    ]
