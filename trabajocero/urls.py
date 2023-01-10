"""trabajocero URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from sasha.views import (index, PostListar, PostCrear,
                               PostActualizar, PostBorrar, PostDetalle,
                               UserSignUp, UserLogin, UserLogout, AvatarActualizar,
                               UserActualizar, MensajeCrear, MensajeDetalle, MensajeListar, miinfo)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sasha/', index, name="sasha_index" ),
    path('sasha/miinfo/', miinfo, name="sasha_miinfo" ),
    path('sasha/listar/', PostListar.as_view(), name="sasha_listar"),
    path('sasha/crear/', PostCrear.as_view(), name="sasha_crear"),
    path('sasha/<int:pk>/actualizar/', PostActualizar.as_view(), name="sasha_actualizar"),
    path('sasha/<int:pk>/borrar/', PostBorrar.as_view(), name="sasha_borrar"),
    path('sasha/<int:pk>/detalle/', PostDetalle.as_view(), name="sasha_detalle"),
    path('sasha/signup/', UserSignUp.as_view(), name="sasha_signup"),
    path('sasha/login/', UserLogin.as_view(), name="sasha_login"),
    path('sasha/logout/', UserLogout.as_view(), name="sasha_logout"),
    path('sasha/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="sasha_avatars_actualizar"),
    path('sasha/users/<int:pk>/actualizar/', UserActualizar.as_view(), name="sasha_users_actualizar"),
    path('sasha/mensajes/crear/', MensajeCrear.as_view(), name="sasha_mensajes_crear"),
    path('sasha/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name="sasha_mensajes_detalle"),
    path('sasha/mensajes/listar/', MensajeListar.as_view(), name="sasha_mensajes_listar"),
  
    
    ]




urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
