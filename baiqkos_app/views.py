from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.db.models import Count
from django.contrib import messages

from .models import Kos, FotoKos, Pemesanan
from .forms import PemesananForm

def tanya_pemilik(request, id):
    kos = Kos.objects.get(id=id)
    nomor_hp_pemilik = kos.pemilik.nomor_hp
    nama_pemilik = kos.pemilik.pemilik
    pesan = f"*Assalamualaikum wr.wb {nama_pemilik}*, bisa saya tanya lebih lanjut terkait kos *{kos.nama}*?"
    url_whatsapp = f"https://wa.me/{nomor_hp_pemilik}/?text={pesan}"
    return redirect(url_whatsapp)

# Create your views here.
def index(request):
    kos = Kos.objects.all().order_by('-id')
    
    # Pencarian
    query = request.GET.get('q')
    if query:
        kos = kos.filter(Q(nama__icontains=query) | Q(alamat__icontains=query))
    
    # Filter Jenis Kos
    jenis = request.GET.get('jenis')
    if jenis:
        kos = kos.filter(jenis=jenis)
    
    # Filter Alamat
    alamat_list = Kos.objects.values_list('alamat', flat=True).distinct()
    alamat = request.GET.get('alamat')
    if alamat:
        kos = kos.filter(alamat=alamat)
    
    return render(request, 'index.html', {'kos': kos, 'alamat_list': alamat_list})


def detail(request, id):
    kos = Kos.objects.prefetch_related('fotos').get(id=id)
    return render(request, 'detail.html', {'kos': kos})

def form_sewa(request):
    if request.method == 'POST':
        form = PemesananForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.mulai_sewa = request.POST.get('mulai_sewa')
            # Setel nilai bidang kos ke nilai yang diterima dari permintaan POST
            form.instance.kos_id = request.POST.get('kos')  
            messages.success(request, f"Selamat, Pengajuan Sewa Berhasil!")
            form.save()
            return redirect('index')
        else:
            messages.error(request, f"Mohon maaf Pengajuan Sewa Gagal, Silahkan Coba Kembali!")
            print('erorr broh...',form.errors)
    else:
        kos_id = request.GET.get('kos_id')
        # Inisialisasi bidang kos dengan nilai yang sesuai
        form = PemesananForm(initial={'kos': kos_id}) 
    context ={
        'form':form,
    }
    return render(request, 'form_sewa.html', context)

@csrf_exempt
def like_kos(request, id):
    if request.method == 'POST':
        kos = Kos.objects.get(id=id)
        kos.suka += 1
        kos.save()
        return JsonResponse({'suka': kos.suka})

def pusat_bantuan(request):
    return render(request, 'pusat_bantuan.html')

def syarat_ketentuan(request):
    return render(request, 'syarat_ketentuan.html')