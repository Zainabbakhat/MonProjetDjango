

from django.shortcuts import render, redirect
from .models import DeliveryInfo
from .forms import DeliveryInfoForm
from django.contrib.auth.decorators import login_required

@login_required
def add_delivery_info(request):
    if request.method == 'POST':
        form = DeliveryInfoForm(request.POST)
        if form.is_valid():
            delivery_info = form.save(commit=False)
            delivery_info.utilisateur = request.user
            delivery_info.save()
            return redirect('list_delivery_info')
    else:
        form = DeliveryInfoForm()
    return render(request, 'delivery/add_delivery_info.html', {'form': form})

@login_required
def list_delivery_info(request):
    delivery_infos = DeliveryInfo.objects.filter(utilisateur=request.user)
    return render(request, 'delivery/list_delivery_info.html', {'delivery_infos': delivery_infos})

@login_required
def edit_delivery_info(request, id):
    delivery_info = DeliveryInfo.objects.get(pk=id, utilisateur=request.user)
    if request.method == 'POST':
        form = DeliveryInfoForm(request.POST, instance=delivery_info)
        if form.is_valid():
            form.save()
            return redirect('list_delivery_info')
    else:
        form = DeliveryInfoForm(instance=delivery_info)
    return render(request, 'delivery/edit_delivery_info.html', {'form': form})

@login_required
def delete_delivery_info(request, id):
    DeliveryInfo.objects.get(pk=id, utilisateur=request.user).delete()
    return redirect('list_delivery_info')

