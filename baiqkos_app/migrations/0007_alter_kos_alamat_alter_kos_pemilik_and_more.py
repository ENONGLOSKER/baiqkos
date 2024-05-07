# Generated by Django 5.0.3 on 2024-05-06 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baiqkos_app', '0006_alter_pemesanan_tanggal_pesan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kos',
            name='alamat',
            field=models.TextField(default='Anjani - Suralaga.Anjani'),
        ),
        migrations.AlterField(
            model_name='kos',
            name='pemilik',
            field=models.CharField(default='Bapak ', max_length=50),
        ),
        migrations.AlterField(
            model_name='kos',
            name='persyaratan',
            field=models.TextField(blank=True, default='Bisa bayar DP (uang muka) : 30%', null=True),
        ),
    ]