from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
import datetime
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
from .forms import Fill_profile_information
from .forms import Register_pool
from .forms import Register_pool_image
from .forms import Register_pool_pack
from .forms import Register_pool_suply
from .forms import Register_provider
from .forms import Contract_text
from .forms import Contract_Rent_text
from .forms import Date
from django.db import models
#from .forms import Register_pool_information
from .models import Informacion_Usuario
from .models import Picina
from .models import Galeria_picina
from .models import Paquete_picina
from .models import Añadido_paquete_picina
from .models import Suministro_picina
from .models import Proveedor
from .models import Contrato_texto 
from .models import cita
from .models import Contrato_rentado
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
                return redirect('/Profile')
            except:
                return render(request, 'Profile_Information_Form.html',{
                    'form': Fill_profile_information,
                    'error': 'Por favor, ingrese sus datos correctamente'
                })
    else:
        return redirect('/Profile')

def Edit_personal_information(request):
    usuario = request.user
    User_inf = get_object_or_404(Informacion_Usuario, user = usuario.id) 
    form = Fill_profile_information(instance = User_inf)
    if request.method == 'GET':
        return render(request, 'Edit_personal_information.html', {
            'form': form
        })
    else:
        form = Fill_profile_information(request.POST, instance = User_inf)
        form.save()
        return redirect('/Profile')

def Register_pools(request):
    if request.method == 'GET':
        return render(request, 'Register_pool.html', {
            'form': Register_pool
        })
    else:
        try:
            return render(request, 'Register_pool.html', {
            'form': Register_pool
        })
        except:
            return render(request, 'Register_pool.html', {
                'form': Register_pool,
                'error': 'Por favor, ingrese sus datos correctamente'
            })

def My_pools(request):
    User_pools = Picina.objects.filter(user=request.user)
    if len(User_pools) < 1:
        if request.method == 'GET':
            return render(request, 'Register_pool.html', {
                'form': Register_pool
            })
        else:
            try:
                form = Register_pool(request.POST,  request.FILES)
                Profile_Information = form.save(commit = False)
                Profile_Information.user = request.user
                Profile_Information.save()
                return redirect("/Profile/My_pools")
            except:
                return render(request, 'Register_pool.html', {
                    'form': Register_pool,
                    'error': "Por favor, ingresar los datos correctamente"
                })
    else:
        return render(request, 'My_pool.html', {
            'User_pools': User_pools
        })

def Galeries(request, Picina_id):
    pool = get_object_or_404(Picina, pk=Picina_id, user = request.user)
    Pool_images = Galeria_picina.objects.filter(picina = pool)
    if request.method == 'GET':
        return render(request, 'Galery.html',{
            'form': Register_pool_image,
            'pool': pool,
            'Pool_images': Pool_images
        })
    else:
        try:
            form = Register_pool_image(request.POST,  request.FILES)
            Profile_Information = form.save(commit = False)
            Profile_Information.picina = pool
            Profile_Information.save()
            return render(request, 'Galery.html',{
                'form': Register_pool_image,
                'pool': pool,
                'Pool_images': Pool_images
            })
        except:
            return render(request, 'Galery.html',{
                'form': Register_pool_image,
                'pool': pool,
                'Pool_images': Pool_images,
                'error': "Por favor, ingresar datos correctos"
            })



def Packs(request, Picina_id):
    pool = get_object_or_404(Picina, pk=Picina_id, user = request.user)
    Pool_packs = Paquete_picina.objects.filter(picina = pool)
    if request.method == 'GET':
            return render(request, 'Packs.html',{
                    'form': Register_pool_pack,
                    'Pool_packs': Pool_packs
                })
    else:
        try:
                form = Register_pool_pack(request.POST)
                Profile_Information = form.save(commit = False)
                Profile_Information.picina = pool
                Profile_Information.save()
                return render(request, 'Packs.html',{
                    'form': Register_pool_pack,
                    'registered': "El paquete fue registrado",
                    'Pool_packs': Pool_packs
                })
        except:
                return render(request, 'Packs.html',{
                    'form': Register_pool_pack,
                    'error': 'Por favor, ingrese sus datos correctamente',
                    'Pool_packs': Pool_packs
                })

def Information(request, Picina_id):
    pool = get_object_or_404(Picina, pk=Picina_id, user = request.user)
    form = Register_pool(instance = pool)
    if request.method == 'GET':
        return render(request, 'Information.html', {
            'form': form
        })
    else:
        try:
            form = Register_pool(request.POST,  request.FILES, instance = pool)
            form.save()
            return redirect('/Profile/My_pools')
        except:
            return render(request, 'Information.html', {
            'form': form,
            'error': "Favor de ingresar los datos correctamente"
        })
            

def Suplies(request, Picina_id):
    pool = get_object_or_404(Picina, pk=Picina_id, user = request.user)
    Pool_suplies = Suministro_picina.objects.filter(picina = pool)
    if  request.method == 'GET':

        return render(request, 'Suplies.html',{
            'form': Register_pool_suply,
            'Pool_suplies': Pool_suplies
        })
    else:
        try:
            form = Register_pool_suply(request.POST)
            Profile_Information = form.save(commit = False)
            Profile_Information.picina = pool
            Profile_Information.save()
            return render(request, 'Suplies.html',{
            'form': Register_pool_suply,
            'error': "Suministro registrado correctamente",
            'Pool_suplies': Pool_suplies
        })
        except:
            return render(request, 'Suplies.html',{
                'form': Register_pool_suply,
                'error': "Por favor ingresar datos validos",
                'Pool_suplies': Pool_suplies
            })

def Providers(request, Picina_id):
    pool = get_object_or_404(Picina, pk=Picina_id, user = request.user)
    Pool_provider = Proveedor.objects.filter(picina = pool)
    if request.method == 'GET':
        return render(request, 'Providers.html',{
            'form': Register_provider,
            'Pool_provider': Pool_provider
        })
    else:
        form = Register_provider(request.POST)
        Profile_Information = form.save(commit = False)
        Profile_Information.picina = pool
        Profile_Information.save()
        return render(request, 'Providers.html',{
            'form': Register_provider,
            'Pool_provider': Pool_provider
        })
    
def Contract(request, Picina_id):
    pool = get_object_or_404(Picina, pk=Picina_id, user = request.user)
    Pool_contract = Contrato_texto.objects.filter(picina = pool)
    if len(Pool_contract) < 1:
        if request.method == 'GET':
            print("Primera vez")
            return render(request, 'New_Contract.html',{
                'form': Contract_text
            })
        else:
            form = Contract_text(request.POST)
            Profile_Information = form.save(commit = False)
            Profile_Information.picina = pool
            Profile_Information.save()
            return redirect('Profile/My_pools/')
    else:
            return render(request, 'Contract.html',{
                'Pool_contract':Pool_contract
            })

def Contract_edit(request, Pool_contract_id):
    Contract = get_object_or_404(Contrato_texto, pk = Pool_contract_id )
    if request.method == 'GET':
        form = Contract_text(instance = Contract)
        return render(request, 'Contract_edit.html',{
            'form': form
        })
    else:
        form = Contract_text(request.POST, instance = Contract)
        form.save()
        return redirect('/Profile/My_pools')

def Consult_pool(request, Pool_name, Pool_id):
    Pool = get_object_or_404(Picina, pk = Pool_id)
    Pack = Paquete_picina.objects.filter(picina = Pool)
    Galery = Galeria_picina.objects.filter(picina = Pool)
    Contact = Informacion_Usuario.objects.filter(user = Pool.user)
    return render(request, 'Consult_pool.html',{
        'Pool': Pool,
        'Galery': Galery,
        'Pack': Pack,
        'Contact': Contact
    })

def Rent_pool(request, Pool_name, Pool_id):
    Pool = get_object_or_404(Picina, pk = Pool_id)
    Packs = Paquete_picina.objects.filter(picina = Pool)
    Extra = Añadido_paquete_picina.objects.filter(picina = Pool)
    Pool_contract = Contrato_texto.objects.filter(picina = Pool)
    if request.method == 'GET':
        return render(request, 'Rent.html',{
            'Date_time': Date,
            'Pool': Pool,
            'Packs': Packs,
            'Extra': Extra,
            'Contract_text': Pool_contract,
        })
    else:        
        try:
            texto = request.POST['ContractTerms']
            fi = request.POST['fecha_inicio']
            hi = request.POST['hora_inicio']
            hf = request.POST['hora_fin']
            try:                
                SaveDateForm = Contract_Rent_text()
                SaveDate = SaveDateForm.save(commit = False)
                SaveDate.contenido = texto
                SaveDate.fecha_inicio = fi
                SaveDate.fecha_fin = fi
                SaveDate.hora_inicio = hi
                SaveDate.hora_fin = hf
                SaveDate.rentero = Pool.id
                SaveDate.cliente = request.user
                SaveDate.save()
            except:
                print(texto)
                print(Pool.id)
                print(request.user)
                print(fi)
                print(hi)
                print(hf)
            return redirect("/Pools/Profile/My_reservation")
        except:
            fi = request.POST['fecha_inicio']
            hi = request.POST['hora_inicio']
            hf = request.POST['hora_fin']
            Dates = Contrato_rentado.objects.filter(rentero = Pool.id, fecha_inicio = fi, hora_inicio__range=[hi, hf], hora_fin__range=[hi, hf])
            if(len(Dates)>0):
                return render(request, 'Rent.html',{
                'Date_time': Date,
                'Pool': Pool,
                'Packs': Packs,
                'Extra': Extra,
                'Contract_text': Pool_contract,
                'error': "La fecha/hora esta mal escrita o esta ocupada"
                })
            else:
                costoTotal = 0
                Pool_contract = Contrato_texto.objects.filter(picina = Pool)
                Extra = Añadido_paquete_picina.objects.filter(picina = Pool)
                Pack = request.POST['inlineRadioOptions']
                Pack_content = get_object_or_404(Paquete_picina, pk = Pack)
                Extra = request.POST.getlist('caja')
                costoTotal += Pack_content.precio
                Extras = []
                format = '%H:%M:%S'
                datetime_str = datetime.datetime.strptime(hf, format)
                datetime_str2 = datetime.datetime.strptime(hi, format)
                timediff = datetime_str - datetime_str2
                toFloat = timediff.total_seconds()
                toFloat = (toFloat/60)/60
                costoTotal += float(toFloat) * Pool.costo_hora
                for i in range (0,len(Extra)):
                    Extras.append(get_object_or_404(Añadido_paquete_picina, pk = Extra[i]))
                    costoTotal += Extras[i].precio

                print(costoTotal)
                return render(request, 'Firm_contract.html',{
                    'Contract_text': Pool_contract,
                    'Pack': Pack_content,
                    'Extras': Extras,
                    'fi': fi,
                    'hi': hi,
                    'hf': hf,
                    'costo_total': costoTotal
                })

def My_reservations(request):
    My_rents = Contrato_rentado.objects.filter(cliente=request.user)
    return render(request, 'My_reservations.html',{
        'My_rents': My_rents,
    })

def My_pool_reservations(request, Picina_id):
    My_pool_rents = Contrato_rentado.objects.filter(rentero = Picina_id)
    return render(request, 'My_pool_reservations.html',{
        'My_pool_rents': My_pool_rents
    })


def View_contract(request,Contract_id):
    Contract = get_object_or_404(Contrato_rentado, pk = Contract_id) 
    Pooldata = get_object_or_404(Picina, pk = Contract.rentero) 
    return render(request, 'View_contract.html',{
        'Contract': Contract,
        'Pooldata': Pooldata
    })