from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Pemilik(models.Model):
    pemilik = models.CharField(max_length=100, default='Bapak')
    nomor_hp = models.CharField(max_length=15)
    def __str__(self) -> str:
        return self.pemilik

# Create your models here.
class Kos(models.Model):
    pemilik = models.ForeignKey(Pemilik, on_delete=models.CASCADE)
    nama = models.CharField(max_length=100)
    alamat = models.TextField(default='Anjani - Suralaga.Anjani')
    jenis = models.CharField(max_length=10, choices=(('Putra', 'Putra'), ('Putri', 'Putri')))
    harga_per_tahun = models.IntegerField()
    sisa_kamar = models.PositiveIntegerField()
    deskripsi = RichTextField(blank=True, null=True)
    fasilitas = RichTextField(blank=True, null=True)
    peraturan = RichTextField(blank=True, null=True)
    persyaratan = RichTextField(blank=True, null=True)
    suka = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nama

class FotoKos(models.Model):
    kos = models.ForeignKey(Kos, on_delete=models.CASCADE, related_name='fotos')
    foto = models.ImageField(upload_to='fotos_kos/')
    deskripsi = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.kos.nama} - {self.deskripsi[:20]}"

class Pemesanan(models.Model):
    kos = models.ForeignKey(Kos, on_delete=models.CASCADE)
    tanggal_pesan = models.DateField(auto_now_add=True, blank=True, null=True)
    penyewa = models.CharField(max_length=100)
    jenis_kelamin = models.CharField(max_length=20)
    mulai_sewa = models.DateField()
    nomor_hp = models.CharField(max_length=15)
    bukti_pembayaran = models.ImageField(upload_to='bukti_pembayaran/')
    ktp = models.ImageField(upload_to='ktp/')
    alamat = models.TextField()
    komfirmasi = models.BooleanField(default=False)

    def __str__(self):
        return f"Pemesanan {self.kos.nama} pada {self.tanggal_pesan}"
