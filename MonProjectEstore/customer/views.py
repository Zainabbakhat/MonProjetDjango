
from django.shortcuts import render,redirect
from customer.models import customer
from customer.formulaire import customerForm


def customer_view(request):
    if request.method == "POST":
        form = customerForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form = customerForm()
    return render(request, 'index.html', {'form': form})
  
def show(request):
    customers = customer.objects.all()  
    return render(request, 'show.html', {'customers': customers})

def edit(request, id):
    customer_instance = customer.objects.get(id=id)  
    return render(request, 'edit.html', {'customer': customer_instance})
def update(request, id):
    customer_instance = customer.objects.get(id=id)  
    form = customerForm(request.POST, instance=customer_instance)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'customer': customer_instance})

def destroy(request, id):
    customer_instance = customer.objects.get(id=id)  
    customer_instance.delete()
    return redirect("/show")

