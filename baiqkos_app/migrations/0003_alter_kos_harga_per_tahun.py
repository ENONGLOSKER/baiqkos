# Generated by Django 5.0.3 on 2024-05-05 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baiqkos_app', '0002_alter_kos_fasilitas_alter_kos_peraturan_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kos',
            name='harga_per_tahun',
            field=models.IntegerField(),
        ),
    ]
