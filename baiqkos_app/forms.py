from django import forms
from .models import Pemesanan

# class PemesananForm(forms.ModelForm):
#     class Meta:
#         model = Pemesanan
#         fields = ['tanggal_mulai', 'nama_lengkap', 'nomor_hp', 'jenis_kelamin', 'foto_ktp', 'bukti_pembayaran', 'alamat']
#         widgets = {
#             'tanggal_mulai': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
#             'nama_lengkap': forms.TextInput(attrs={'class': 'form-control'}),
#             'nomor_hp': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '+62'}),
#             'jenis_kelamin': forms.Select(attrs={'class': 'form-select'}),
#             'foto_ktp': forms.FileInput(attrs={'class': 'form-control'}),
#             'bukti_pembayaran': forms.FileInput(attrs={'class': 'form-control'}),
#             'alamat': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
#         }
