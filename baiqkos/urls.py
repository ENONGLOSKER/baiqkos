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
    path('', views.index, name='index'),
    path('kos/datail/<int:id>/', views.detail, name='detail'),
    path('kos/form-sewa/', views.form_sewa, name='form_sewa'),
    path('suka/<int:id>/', views.like_kos, name='like_kos'),
     path('tanya-pemilik/<int:id>/', views.tanya_pemilik, name='tanya_pemilik'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
