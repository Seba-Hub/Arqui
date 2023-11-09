from django.shortcuts import render, redirect
from .models import Hora
from .forms import HoraForm
from django.contrib import messages



# Create your views here.

def create_hora(request):
    if request.method == 'GET':
        context = {'form': HoraForm()}
        return render(request, 'horas/hora_form.html', context)
    elif request.method == 'POST':
        form = HoraForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'La hora ha sido publicada.')
            return redirect('posts')
        else:
            messages.error(request, 'Corrija este error:')
            return render(request, 'horas/hora_form.html', {'form': form})

def home(request):
    posts = Hora.objects.all()
    context = {'posts': posts}
    return render(request, 'horas/home.html', context)
