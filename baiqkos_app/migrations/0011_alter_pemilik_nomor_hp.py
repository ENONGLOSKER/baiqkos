# Generated by Django 5.0.3 on 2024-05-06 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baiqkos_app', '0010_pemilik_alter_kos_persyaratan_kos_pemilik'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pemilik',
            name='nomor_hp',
            field=models.CharField(max_length=15),
        ),
    ]