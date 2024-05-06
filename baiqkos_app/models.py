from django.db import models

# Create your models here.
class Kos(models.Model):
    pemilik = models.CharField(max_length=50, default='Anonim')
    nama = models.CharField(max_length=100)
    alamat = models.TextField()
    jenis = models.CharField(max_length=10, choices=(('Putra', 'Putra'), ('Putri', 'Putri')))
    harga_per_tahun = models.IntegerField()
    sisa_kamar = models.PositiveIntegerField()
    deskripsi = models.TextField(blank=True, null=True)
    fasilitas = models.TextField(blank=True, null=True)
    peraturan = models.TextField(blank=True, null=True)
    persyaratan = models.TextField(blank=True, null=True)
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

    def __str__(self):
        return f"Pemesanan {self.kos.nama} pada {self.tanggal_pesan}"
