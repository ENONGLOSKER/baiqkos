from django.contrib import admin
from .models import Kos,FotoKos, Pemesanan, Pemilik
from django.utils.safestring import mark_safe

# Register your models here.
@admin.register(Pemilik)
class PemilikAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Pemilik._meta.fields]

@admin.register(Kos)
class KosAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Kos._meta.fields]

@admin.register(FotoKos)
class FotoKosAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'display_foto', 'deskripsi']

    def display_foto(self, obj):
        return mark_safe('<img src="{}" width="50" height="50" />'.format(obj.foto.url))
    display_foto.short_description = 'Foto'


@admin.register(Pemesanan)
class PemesananAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'kos', 'tanggal_pesan', 'penyewa', 'jenis_kelamin', 'mulai_sewa', 'nomor_hp', 'bukti_pembayaran_display', 'ktp_display', 'alamat']
    
    def bukti_pembayaran_display(self, obj):
        return mark_safe('<img src="{}" width="50" height="50" />'.format(obj.bukti_pembayaran.url))
    bukti_pembayaran_display.short_description = 'Bukti Pembayaran'

    def ktp_display(self, obj):
        return mark_safe('<img src="{}" width="50" height="50" />'.format(obj.ktp.url))
    ktp_display.short_description = 'KTP'
