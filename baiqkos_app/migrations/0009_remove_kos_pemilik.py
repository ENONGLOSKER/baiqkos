# Generated by Django 5.0.3 on 2024-05-06 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baiqkos_app', '0008_alter_kos_persyaratan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kos',
            name='pemilik',
        ),
    ]