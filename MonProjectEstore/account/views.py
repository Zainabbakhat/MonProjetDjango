from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import UserProfile


# Create your views here.

def HomePage(request):
    return render(request, 'home.html')

def FournisseurPage(request):
    return render(request, 'fournisseur.html')

    
def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)

        if user is not None:
            login(request, user)

            # Récupérer le UserProfile et vérifier le typeofprofile
            try:
                user_profile = UserProfile.objects.get(user=user)
                typeofprofile = user_profile.typeofprofile

                if typeofprofile == 'fournisseur':
                    return redirect('./fournisseur')  # Redirige vers la page d'accueil des fournisseurs
                elif typeofprofile == 'client':
                    return redirect('./client')  # Redirige vers la page d'accueil des acheteurs
                # Ajoutez plus de conditions si nécessaire
                else:
                    return redirect('home')  # Redirige vers une page d'accueil générale

            except UserProfile.DoesNotExist:
                # Gérer le cas où l'utilisateur n'a pas de profil
                return HttpResponse("UserProfile does not exist for this user")

        else:
            return HttpResponse("username or password is incorrect!")

    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('./loginPage')

def page(request):
   return render(request, 'page.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        typeofprofile = request.POST.get('typeofprofile')  # Récupération du type de profil
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("the password is incorrect")
        my_user=User.objects.create_user(uname,email,pass1)
        my_user.save()
        user_profile = UserProfile(user=my_user, typeofprofile=typeofprofile)
        user_profile.save()
        return redirect('./loginPage')      
    return render(request, 'signup.html')
    if not User.objects.filter(username='uname').exists():
            my_user=User.objects.create_user('uname','email','pass1')
            my_user.save()
    else:
                            return HttpResponse("username exists")   
