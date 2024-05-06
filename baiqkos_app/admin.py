from django.contrib import admin
from .models import Kos,FotoKos, Pemesanan

# Register your models here.
@admin.register(Kos)
class KosAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Kos._meta.fields]

@admin.register(FotoKos)
class FotoKosAdmin(admin.ModelAdmin):
    list_display = [field.name for field in FotoKos._meta.fields]

@admin.register(Pemesanan)
class PemesananAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Pemesanan._meta.fields]
