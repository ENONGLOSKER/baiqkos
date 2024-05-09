"""
URL configuration for baiqkos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from baiqkos_app import views
urlpatterns = [

    path('admin/', admin.site.urls),
    # admin
    path('kos/signout/', views.signout_form, name='signout'),
    path('kos/signin/', views.sigin_form, name='signin'),
    path('kos/dashboard/', views.dashboard, name='dashboard'),
    path('kos/dashboard/pemilik/', views.dashboard_pemilik, name='pemilik'),
    path('kos/dashboard/penyewa/', views.dashboard_pemesan, name='pemesan'),
    path('kos/dashboard/kos/', views.dashboard_kos, name='kos'),
    # user
    path('', views.index, name='index'),
    path('kos/pusat/bantuan/', views.pusat_bantuan, name='pusat_bantuan'),
    path('kos/syarat/ketentuan/', views.syarat_ketentuan, name='syarat_ketentuan'),
    path('kos/datail/<int:id>/', views.detail, name='detail'),
    path('kos/form-sewa/', views.form_sewa, name='form_sewa'),

    path('suka/<int:id>/', views.like_kos, name='like_kos'),
    path('tanya-pemilik/<int:id>/', views.tanya_pemilik, name='tanya_pemilik'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
