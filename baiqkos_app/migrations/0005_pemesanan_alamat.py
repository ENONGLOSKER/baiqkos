# Generated by Django 5.0.3 on 2024-05-06 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baiqkos_app', '0004_kos_pemilik'),
    ]

    operations = [
        migrations.AddField(
            model_name='pemesanan',
            name='alamat',
            field=models.TextField(default=True),
            preserve_default=False,
        ),
    ]