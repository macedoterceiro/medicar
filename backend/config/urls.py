"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from agenda.views import AgendasViewSet
from consulta.views import ConsultasViewSet
from medico.views import MedicosViewSet, EspecialidadesViewSet
from usuario.views import UserRegistrationAPIView, CustomAuthToken

router = routers.DefaultRouter()
router.register(r'especialidades', EspecialidadesViewSet)
router.register(r'medicos', MedicosViewSet)
router.register(r'agendas', AgendasViewSet, basename="agendas")
router.register(r'consultas', ConsultasViewSet, basename="consultas")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', CustomAuthToken.as_view()),
    path('registrar/', UserRegistrationAPIView.as_view()),
    path('', include(router.urls))
]