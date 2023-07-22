from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # Importe a função redirect

def redirect_to_login(request):
    return redirect('inventory:login')

urlpatterns = [
    path('', redirect_to_login),  # Redirecione a raiz para a página de login
    path('admin/', admin.site.urls),
    path('inventory/', include('inventory.urls')),
]
