from django.shortcuts import render, redirect
from .models import Kos, FotoKos, Pemesanan
# from .forms import PemesananForm

# Create your views here.
def index(request):
    kos = Kos.objects.prefetch_related('fotos').all()
    return render(request, 'index.html', {'kos': kos})

def detail(request, id):
    kos = Kos.objects.prefetch_related('fotos').get(id=id)
    return render(request, 'detail.html', {'kos': kos})

def form_sewa(request):
    # if request.method == 'POST':
    #     form = PemesananForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('index')
    # else:
    #     form = PemesananForm()
    return render(request, 'form_sewa.html')


