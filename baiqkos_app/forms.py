# Di file forms.py di aplikasi Anda

from django import forms
from .models import Pemesanan

# Di file forms.py

class PemesananForm(forms.ModelForm):
    JENIS_KELAMIN_CHOICES = [
        ('Laki-laki', 'Laki-laki'),
        ('Perempuan', 'Perempuan'),
    ]

    jenis_kelamin = forms.ChoiceField(choices=JENIS_KELAMIN_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = Pemesanan
        fields = ['kos', 'penyewa', 'nomor_hp', 'jenis_kelamin', 'mulai_sewa', 'bukti_pembayaran', 'ktp', 'alamat']
        widgets = {
            'kos': forms.HiddenInput(), 
            'mulai_sewa': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'penyewa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama User'}),
            'nomor_hp': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '08511111111'}),
            'bukti_pembayaran': forms.FileInput(attrs={'class': 'form-control'}),
            'ktp': forms.FileInput(attrs={'class': 'form-control'}),
            'alamat': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Dusun, Desa, Kec-Kab'}),
        }
        labels = {
            'mulai_sewa': 'Tanggal Mulai', 
            'ktp': 'Foto KTP'  
        }
