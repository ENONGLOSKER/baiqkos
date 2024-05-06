from django.shortcuts import render, redirect
from .models import Kos, FotoKos, Pemesanan
from .forms import PemesananForm

# Create your views here.
def index(request):
    kos = Kos.objects.prefetch_related('fotos').all()
    return render(request, 'index.html', {'kos': kos})

def detail(request, id):
    kos = Kos.objects.prefetch_related('fotos').get(id=id)
    return render(request, 'detail.html', {'kos': kos})

# Di file views.py

def form_sewa(request):
    if request.method == 'POST':
        form = PemesananForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.mulai_sewa = request.POST.get('mulai_sewa')
            form.save()
            return redirect('index') 
    else:
        kos_id = request.GET.get('kos_id')  # Mengambil ID kos dari query parameter
        form = PemesananForm(initial={'kos': kos_id})  # Mengatur nilai awal kos berdasarkan ID yang diterima
    context ={
        'form':form,
    }
    return render(request, 'form_sewa.html', context)



