from django.forms import ModelForm
from .models import Informacion_Usuario
from .models import Picina
from .models import Galeria_picina
from .models import Paquete_picina
from .models import Añadido_paquete_picina
from .models import Proveedor
from .models import Suministro_picina
from .models import Contrato_texto

class Fill_profile_information(ModelForm):
    class Meta:
        model = Informacion_Usuario
        fields = ['nombre', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento', 'direccion', 'correo_electronico', 'telefono_contacto']
        
class Register_pool(ModelForm):
    class Meta:
        model = Picina
        fields = ['nombre','direccion', 'descripcion','costo_hora','imagen']
    
class Register_pool_image(ModelForm):
    class Meta:
        model = Galeria_picina
        fields = ['imagen', 'descripcion']

class Register_pool_pack(ModelForm):
    class Meta:
        model = Paquete_picina
        fields = ['nombre', 'descripcion', 'precio']

class Register_pool_axtra(ModelForm):
    class Meta:
        model = Añadido_paquete_picina
        fields = ['nombre', 'descripcion', 'precio']

class Register_pool_suply(ModelForm):
    class Meta:
        model = Suministro_picina
        fields = ['nombre', 'descripcion', 'cantidad_inventario']

class Register_provider(ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre','descripcion','telefono_contacto','correo_electronico']

class Contract_text(ModelForm):
    class Meta:
        model = Contrato_texto
        fields = ['texto']