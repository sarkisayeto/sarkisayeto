from django.shortcuts import get_object_or_404, render, redirect
from .forms import MiseAJourForm
from .models import MiseAJour

def update_form(request):
    if request.method == 'POST':
        form = MiseAJourForm(request.POST)
        if form.is_valid():
           form.save()
           form = MiseAJourForm()  # Clear form for next use.  # noqa: F841
    else:
        form = MiseAJourForm()
    return render(request, 'update_form.html', {'form': form})

def update_history(request):
    brel_eco_updates = MiseAJour.objects.filter(type_logiciel='Brel-Eco')
    brel_gest_updates = MiseAJour.objects.filter(type_logiciel='Brel-Gest')
    
    return render(request, 'update_history.html', {
        'brel_eco_updates': brel_eco_updates,
        'brel_gest_updates': brel_gest_updates,
    })

def modifier_update(request, id):
    update = get_object_or_404(MiseAJour, id=id)
    if request.method == 'POST':
        form = MiseAJourForm(request.POST, instance = update)
        if form.is_valid():
            form.save()
        return redirect('update_history')
    else:
        form = MiseAJourForm(instance = update)
    return render(request, 'modifier_update.html', {'form':form})
