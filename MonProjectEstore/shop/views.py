from django.shortcuts import redirect, render
from .models import Product, Commande
from django.core.paginator import Paginator
from django.urls import reverse
from django.conf import settings


# Create your views here.
def index(request):
    product_object = Product.objects.all()
    item_name = request.GET.get('item-name')
    if item_name !='' and item_name is not None:
     product_object = Product.objects.filter(title__icontains=item_name)
    paginator = Paginator(product_object, 4)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)
    return render(request, 'shop/index.html', {'product_object': product_object})

def detail(request, id):
    product_object = Product.objects.get(id=id)
    return render(request, 'shop/detail.html', {'product': product_object}) 

def checkout(request):
  
    if request.method == "POST":
        items = request.POST.get('items')
        total = request.POST.get('total')
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        adresse = request.POST.get('adresse')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        zipcode= request.POST.get('zipcode')
        com = Commande(items=items,total=total, nom=nom, email=email, adresse=adresse, ville=ville, pays=pays, zipcode=zipcode)
        com.save()
        return redirect('shop:confirmation')


    return render(request, 'shop/checkout.html') 
 

def confirmation(request):
    info = Commande.objects.all()[:1]
    for item in info:
        nom = item.nom
    return render(request, 'shop/confirmation.html', {'name': nom})


def payment_completed_view(request):
    return render(request, 'core/payement-completed.html')
                  

def payment_failed_view(request):
    return render(request, 'core/payement-failed.html')
 
    
     
           

   
