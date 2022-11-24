from django.contrib import admin
from .models import Informacion_Usuario
from .models import Picina
from .models import Galeria_picina
from .models import Paquete_picina
from .models import Añadido_paquete_picina
from .models import Proveedor
from .models import Suministro_picina
from .models import Contrato_texto
from .models import Contrato_rentado
from .models import cita
# Register your models here.
admin.site.register(Informacion_Usuario)
admin.site.register(Picina)
admin.site.register(Galeria_picina)
admin.site.register(Paquete_picina)
admin.site.register(Añadido_paquete_picina)
admin.site.register(Proveedor)
admin.site.register(Suministro_picina)
admin.site.register(Contrato_texto)
admin.site.register(Contrato_rentado)
admin.site.register(cita)