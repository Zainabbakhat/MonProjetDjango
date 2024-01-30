from django.shortcuts import render,redirect
from .models import supplier
from .forms import SupplierForm

def suppliers(request):
    if request.method=="POST":
        form= SupplierForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/supplier_show")
            except:
                pass
    else:
            form=SupplierForm()
    return render(request,'supplier_form.html',{'form': form}) 

def show(request):
    suppliers = supplier.objects.all()
    context = {'suppliers': suppliers}
    return render(request, 'supplier_show.html', context)



