"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sara import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name = 'Home'),
    path('Signup/', views.Signup, name = 'Signup'),
    path('Logout/', views.Signout, name = 'Logout'),
    path('Signin/', views.Signin, name = 'Signin'),
    path('Profile/', views.Profile, name = 'Profile'),
    path('Profile/Information/', views.Fill_information, name = 'Profile_information'),
    path('Profile/My_pools', views.My_pools, name = 'My_pools'),
    path('Profile/New_pool', views.Register_pools, name = 'Register_pool'),
    path('Profile/My_pools/Packs/<int:Picina_id>', views.Packs, name = 'Packs'),
    path('Profile/My_pools/Suplies/<int:Picina_id>', views.Suplies, name = 'Suplies'),
    path('Profile/My_pools/Galery/<int:Picina_id>', views.Galeries, name = 'Galeries'),
    path('Profile/My_pools/Information/<int:Picina_id>', views.Information, name = 'Information'),
    path('Profile/My_pools/Providers/<int:Picina_id>', views.Providers, name = 'Providers'),
    path('Profile/My_pools/Contract/<int:Picina_id>', views.Contract, name = 'Contract'),
    path('Profile/My_pools/Contract/Edit/<int:Pool_contract_id>', views.Contract_edit, name = 'Contract_edit'),
    path('Profile/Edit/Pesonal-Information', views.Edit_personal_information, name = 'Edit_personal_information'),
    path('Pools/<str:Pool_name>/<int:Pool_id>', views.Consult_pool, name = 'Consult_pool'),
    path('Pools/Rent/<str:Pool_name>/<int:Pool_id>', views.Rent_pool, name = 'Rent_pool'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
