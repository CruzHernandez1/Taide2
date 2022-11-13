from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from .forms import Fill_profile_information
from .forms import Register_pool
from .forms import Register_pool_image
from .forms import Register_pool_pack
from .forms import Register_pool_suply
#from .forms import Register_pool_information
from .models import Informacion_Usuario
from .models import Picina
from .models import Galeria_picina
from .models import Paquete_picina
from .models import Añadido_paquete_picina
from .models import Suministro_picina
from .models import Proveedor

# Create your views here.
def Home(request):
    Pools = Picina.objects.all()
    return render(request, 'Home.html', {
        'Pools': Pools
    })

def Signup(request):
    if(request.method == 'GET'):
        return render(request, 'Signup.html',{
        'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # register user
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('Home')
                
            except IntegrityError:
                return render(request, 'Signup.html',{
                    'form': UserCreationForm,
                    "error": 'Este nombre de usuario ya esta ocupado'
                })
        return render(request, 'Signup.html',{
                    'form': UserCreationForm,
                    "error": 'Las contraseñas no coinciden'
                })
def Signout(request):
    logout(request)
    return redirect('Home')
        
def Signin(request):
    if request.method == 'GET':
        return render(request, 'Signin.html',{
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        
        if user is None:
            return render(request, 'Signin.html',{
            'form': AuthenticationForm,
            'error': 'El usuario o contraseña no son correctos'
            })
            return render(request, 'Signin.html',{
                'form': AuthenticationForm
            })
        else:
            login(request, user)
            return redirect('Home')

def Profile(request):
    User_inf = Informacion_Usuario.objects.filter(user=request.user)
    if len(User_inf) < 1:
        return render(request, 'ProfileNotFill.html')
    else:
        return render(request, 'Profile.html', {'User_inf': User_inf})

def Fill_information(request):
    User_inf = Informacion_Usuario.objects.filter(user=request.user)
    if len(User_inf) < 1:
        if request.method == 'GET':
            return render(request, 'Profile_Information_Form.html',{
                    'form': Fill_profile_information
                })
        else:
            try:
                form = Fill_profile_information(request.POST)
                Profile_Information = form.save(commit = False)
                Profile_Information.user = request.user
                Profile_Information.save()
                return render(request, 'Profile_Information_Form.html',{
                    'form': Fill_profile_information
                }) 
            except:
                return render(request, 'Profile_Information_Form.html',{
                    'form': Fill_profile_information,
                    'error': 'Por favor, ingrese sus datos correctamente'
                })
    else:
        return redirect('/Profile')

def Register_pools(request):
    return render(request, 'Register_pool.html', {
        'form': Register_pool,
        'error': 'Por favor, ingrese sus datos correctamente'
        })

def My_pools(request):
    User_pools = Picina.objects.filter(user=request.user)
    return render(request, 'My_pool.html', {
        'User_pools': User_pools
        })

def Galeries(request, Picina_id):
    pool = get_object_or_404(Picina, pk=Picina_id, user = request.user)

    Pool_images = Galeria_picina.objects.filter(picina = pool)
    return render(request, 'Galery.html',{
        'form': Register_pool_image,
        'pool': pool,
        'Pool_images': Pool_images
    })

def Packs(request, Picina_id):
    pool = get_object_or_404(Picina, pk=Picina_id, user = request.user)
    Pool_packs = Paquete_picina.objects.filter(picina = pool)
    return render(request, 'Packs.html', {
        'form': Register_pool_pack,
        'error': "Por favor ingresar datos validos",
        'Pool_packs': Pool_packs
    })

def Information(request, Picina_id):
    return render(request, 'Packs.html', {
        'form': Register_pool_information
    })

def Suplies(request, Picina_id):
    pool = get_object_or_404(Picina, pk=Picina_id, user = request.user)
    Pool_suplies = Suministro_picina.objects.filter(picina = pool)
    return render(request, 'Suplies.html',{
        'form': Register_pool_suply,
        'error': "Por favor ingresar datos validos",
        'Pool_suplies': Pool_suplies
    })

    


        



