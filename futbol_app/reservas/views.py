
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cancha, Reserva
from django.utils.timezone import now

@login_required
def listar_canchas(request):
    canchas = Cancha.objects.all()
    return render(request, 'reservas/canchas.html', {'canchas': canchas})

@login_required
def agregar_cancha(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        ubicacion = request.POST.get('ubicacion')
        Cancha.objects.create(nombre=nombre, ubicacion=ubicacion)
        return redirect('listar_canchas')
    return render(request, 'reservas/agregar_cancha.html')

@login_required
def reservar_cancha(request, cancha_id):
    cancha = get_object_or_404(Cancha, id=cancha_id)
    if request.method == 'POST':
        fecha = request.POST.get('fecha')
        Reserva.objects.create(usuario=request.user, cancha=cancha, fecha=fecha)
        return redirect('listar_reservas')
    return render(request, 'reservas/reservar_cancha.html', {'cancha': cancha})

@login_required
def listar_reservas(request):
    reservas = Reserva.objects.filter(usuario=request.user).order_by('-fecha')
    return render(request, 'reservas/reservas.html', {'reservas': reservas})
