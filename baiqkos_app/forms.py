from django import forms
from .models import Pemesanan, Pemilik, Kos, FotoKos
from django.core.exceptions import ValidationError

class KosForm(forms.ModelForm):
    class Meta:
        model = Kos
        fields = "__all__"

        widgets = {
            'pemilik':forms.Select(attrs={'class':'form-control'}),
            'nama':forms.TextInput(attrs={'class':'form-control'}),
            'alamat':forms.TextInput(attrs={'class':'form-control'}),
            'jenis':forms.Select(attrs={'class':'form-control'}),
            'harga_per_tahun':forms.NumberInput(attrs={'class':'form-control'}),
            'sisa_kamar':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'+6285337802822'}),
            'deskripsi':forms.Textarea(attrs={'class':'form-control', 'placeholder':'+6285337802822'}),
            'fasilitas':forms.Textarea(attrs={'class':'form-control', 'placeholder':'+6285337802822'}),
            'peraturan':forms.Textarea(attrs={'class':'form-control', 'placeholder':'+6285337802822'}),
            'persyaratan':forms.TextInput(attrs={'class':'form-control', 'placeholder':'+6285337802822'}),
        }

class FotoKosForm(forms.ModelForm):
    class Meta:
        model = FotoKos
        fields = "__all__"

        widgets = {
            'kos':forms.Select(attrs={'class':'form-control'}),
            'foto':forms.FileInput(attrs={'class': 'form-control'}),
            'deskripsi':forms.Textarea(attrs={'class':'form-control', 'placeholder':'+6285337802822'}),
        }

class PemilikForm(forms.ModelForm):
    class Meta:
        model = Pemilik
        fields = "__all__"

        widgets = {
            'pemilik':forms.TextInput(attrs={'class':'form-control'}),
            'nomor_hp':forms.TextInput(attrs={'class':'form-control', 'placeholder':'+6285337802822'}),
        }

class PemesananForm(forms.ModelForm):
    JENIS_KELAMIN_CHOICES = [
        ('L', 'Laki-laki'),
        ('P', 'Perempuan'),
    ]

    jenis_kelamin = forms.ChoiceField(choices=JENIS_KELAMIN_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}), label='Jenis Kelamin')

    class Meta:
        model = Pemesanan
        fields = ['kos', 'penyewa', 'nomor_hp', 'jenis_kelamin', 'mulai_sewa', 'bukti_pembayaran', 'ktp', 'alamat']
        widgets = {
            'kos': forms.HiddenInput(), 
            # 'kos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'kos'}),
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

    def clean(self):
        cleaned_data = super().clean()
        bukti_pembayaran = cleaned_data.get('bukti_pembayaran')
        ktp = cleaned_data.get('ktp')

        if not bukti_pembayaran and not ktp:
            raise ValidationError("Mohon unggah setidaknya satu bukti pembayaran atau KTP.")
