from django.shortcuts import render, redirect
from .models import EntradaDiario
from .forms import DiarioForm


def home(request):
    if request.method == 'POST':
        form = DiarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DiarioForm()
    
    entradas = EntradaDiario.objects.all().order_by('-criado_em')
    return render(request, 'diario.html', {'form': form, 'entradas': entradas})
