from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, F
from django.http import JsonResponse
from django.db.models.functions import TruncDate
from datetime import date

from .models import Kos, FotoKos, Pemesanan, Pemilik
from .forms import PemesananForm, PemilikForm, KosForm, FotoKosForm

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
            pemesanan = form.save(commit=False)
            pemesanan.mulai_sewa = request.POST.get('mulai_sewa')
            pemesanan.kos_id = request.POST.get('kos')  
            messages.success(request, f"Selamat, Pengajuan Sewa Berhasil!")
            pemesanan.save()

            # Kurangi sisa kamar pada kos yang dipilih
            kos = get_object_or_404(Kos, id=pemesanan.kos_id)
            kos.sisa_kamar -= 1
            kos.save()

            return redirect('index')
        else:
            messages.error(request, f"Mohon maaf Pengajuan Sewa Gagal, Silahkan Coba Kembali!")
            print('error broh...', form.errors)
    else:
        kos_id = request.GET.get('kos_id')
        # Inisialisasi bidang kos dengan objek Kos yang sesuai
        kos = get_object_or_404(Kos, id=kos_id)
        form = PemesananForm(initial={'kos': kos}) 
    context ={
        'form': form,
    }
    return render(request, 'form_sewa.html', context)

def pusat_bantuan(request):
    return render(request, 'pusat_bantuan.html')

def syarat_ketentuan(request):
    return render(request, 'syarat_ketentuan.html')

@csrf_exempt
def like_kos(request, id):
    if request.method == 'POST':
        kos = Kos.objects.get(id=id)
        kos.suka += 1
        kos.save()
        return JsonResponse({'suka': kos.suka})

def tanya_pemilik(request, id):
    kos = Kos.objects.get(id=id)
    nomor_hp_pemilik = kos.pemilik.nomor_hp
    nama_pemilik = kos.pemilik.pemilik
    pesan = f"*Assalamualaikum wr.wb {nama_pemilik}*, bisa saya tanya lebih lanjut terkait kos *{kos.nama}*?"
    url_whatsapp = f"https://wa.me/{nomor_hp_pemilik}/?text={pesan}"
    return redirect(url_whatsapp)


# ADMIN -------------------------------------------------------------------------------------
def signout_form(request):
    logout(request)
    return redirect('index')

def sigin_form(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Sign in Berhasil, Selamat datang {user}")
            return redirect('dashboard')
        else:
            messages.error(request, "Sign in Gagal, Silahkan coba kembali!")
            return redirect('signin')
    elif request.user.is_authenticated:
        return redirect('dashboard')
    
    return render(request, 'signin.html')

def dashboard(request):
    # Mengambil data total pemesanan per tanggal
    pemesanan_per_tanggal = Pemesanan.objects.annotate(date=TruncDate('tanggal_pesan')).values('date').annotate(total=Count('id'))

    # Mengambil data pembagian jenis kelamin pemesan
    pembagian_jenis_kelamin = Pemesanan.objects.values('jenis_kelamin').annotate(total=Count('id'))

    return render(request, 'dashboard01.html', {
        'pemesanan_per_tanggal': pemesanan_per_tanggal,
        'pembagian_jenis_kelamin': pembagian_jenis_kelamin,
    })

# dashboard pemilik
def dashboard_pemilik(request):
    cari = request.GET.get('cari')  # Mendapatkan parameter pencarian dari URL
    if cari:  # Jika ada parameter pencarian
        data = Pemilik.objects.filter(pemilik__icontains=cari)  # Melakukan pencarian berdasarkan nama pemilik
    else:  # Jika tidak ada parameter pencarian, tampilkan semua data
        data = Pemilik.objects.all()

    paginator = Paginator(data, 5)  # Memisahkan data menjadi beberapa halaman, 10 data per halaman
    page_number = request.GET.get('page')  # Mendapatkan nomor halaman dari parameter URL
    try:
        datas = paginator.page(page_number)
    except PageNotAnInteger:
        datas = paginator.page(1)
    except EmptyPage:
        datas = paginator.page(paginator.num_pages)

    context = {
        'datas': datas,
    }
    return render(request, 'dashboard02.html', context)

def pemilik_tambah(request):
    if request.method == 'POST':
        form = PemilikForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pemilik')
    else:
        form = PemilikForm()

    context = { 
        'form':form,
    }

    return render(request, 'dashboard_form.html', context)

def pemilik_update(request, id):
    pemilik = Pemilik.objects.get(id=id)
    if request.method == 'POST':
        form = PemilikForm(request.POST, instance=pemilik)
        if form.is_valid():
            form.save()
            return redirect('pemilik')
    else:
        form = PemilikForm(instance=pemilik)

    context = { 
        'form':form,
    }

    return render(request, 'dashboard_form.html', context)

def pemilik_delete(request, id):
    pemilik = Pemilik.objects.get(id=id)
    pemilik.delete()
    return redirect('pemilik')

# dashboard pemesan
def dashboard_pemesan(request):
    cari = request.GET.get('cari')  # Mendapatkan parameter pencarian dari URL
    if cari:  # Jika ada parameter pencarian
        data = Pemesanan.objects.filter(penyewa__icontains=cari)  # Melakukan pencarian berdasarkan nama penyewa
    else:  # Jika tidak ada parameter pencarian, tampilkan semua data
        data = Pemesanan.objects.all()

    paginator = Paginator(data, 3)  # Memisahkan data menjadi beberapa halaman, 10 data per halaman
    page_number = request.GET.get('page')  # Mendapatkan nomor halaman dari parameter URL
    
    tanggal_sekarang = date.today()

    try:
        datas = paginator.page(page_number)
    except PageNotAnInteger:
        datas = paginator.page(1)
    except EmptyPage:
        datas = paginator.page(paginator.num_pages)
    context = {
        'datas': datas,
        'tanggal_sekarang': tanggal_sekarang,
    }
    return render(request, 'dashboard03.html', context)


def pemesan_tambah(request):
    if request.method == 'POST':
        form = PemesananForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pemesan')
    else:
        form = PemesananForm()

    context = { 
        'form':form,
    }

    return render(request, 'dashboard_form.html', context)

def pemesan_update(request, id):
    pemesan = Pemesanan.objects.get(id=id)
    if request.method == 'POST':
        form = PemesananForm(request.POST, instance=pemesan)
        if form.is_valid():
            form.save()
            return redirect('pemesan')
    else:
        form = PemesananForm(instance=pemesan)

    context = { 
        'form':form,
    }

    return render(request, 'dashboard_form.html', context)

def pemesan_delete(request, id):
    pemesan = Pemesanan.objects.get(id=id)
    pemesan.delete()
    return redirect('pemesan')

# dashboard kos
def dashboard_kos(request):
    cari = request.GET.get('cari')  # Mendapatkan parameter pencarian dari URL
    if cari:  # Jika ada parameter pencarian
        data = Kos.objects.filter(nama__icontains=cari)  # Melakukan pencarian berdasarkan nama kos
    else:  # Jika tidak ada parameter pencarian, tampilkan semua data
        data = Kos.objects.all()

    paginator = Paginator(data, 3)  # Memisahkan data menjadi beberapa halaman, 10 data per halaman
    page_number = request.GET.get('page')  # Mendapatkan nomor halaman dari parameter URL
    try:
        datas = paginator.page(page_number)
    except PageNotAnInteger:
        datas = paginator.page(1)
    except EmptyPage:
        datas = paginator.page(paginator.num_pages)

    context = {
        'datas': datas,
    }
    return render(request, 'dashboard04.html', context)

def kos_tambah(request):
    if request.method == 'POST':
        form = KosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kos')
    else:
        form = KosForm()

    context = { 
        'form':form,
    }

    return render(request, 'dashboard_form.html', context)

def kos_update(request, id):
    kos = Kos.objects.get(id=id)
    if request.method == 'POST':
        form = KosForm(request.POST, instance=kos)
        if form.is_valid():
            form.save()
            return redirect('kos')
    else:
        form = KosForm(instance=kos)

    context = { 
        'form':form,
    }

    return render(request, 'dashboard_form.html', context)

def kos_delete(request, id):
    kos = Kos.objects.get(id=id)
    kos.delete()
    return redirect('kos')

# dashboard foto kos
def dashboard_foto_kos(request, id):
    kos = get_object_or_404(Kos, id=id)  # Menggunakan get_object_or_404 untuk mendapatkan satu objek Kos berdasarkan id
    data = kos.fotos.all()  # Menggunakan atribut 'fotos' untuk mendapatkan semua foto terkait kos tersebut
    context = {
        'kos': kos,
        'datas': data,
    }
    return render(request, 'dashboard05.html', context)

def foto_kos_tambah(request):
    if request.method == 'POST':
        form = FotoKosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('kos')
    else:
        form = FotoKosForm()

    context = { 
        'form':form,
    }

    return render(request, 'dashboard_form.html', context)

def foto_kos_update(request, id):
    foto_kos = get_object_or_404(FotoKos, id=id)
    if request.method == 'POST':
        form = FotoKosForm(request.POST, instance=foto_kos)
        if form.is_valid():
            form.save()
            return redirect('kos')
    else:
        form = FotoKosForm(instance=foto_kos)

    context = { 
        'form':form,
    }

    return render(request, 'dashboard_form.html', context)

def foto_kos_delete(request, id):
    foto_kos = get_object_or_404(FotoKos, id=id)
    foto_kos.delete()
    return redirect('kos')
