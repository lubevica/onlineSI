"""misitio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

#from curso import views
from curso.views import inicio
from cdictadas.views import pclases
from equipo.views import pequipo
from noticias.views import pnoticias
from ayudantias.views import payudantias
from ranking.views import pranking
from equipo.views import pcoordinador
from equipo.views import payudantesa
from equipo.views import payudantesd


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^inicio/', inicio),
    url(r'^pclases/', pclases),
    url(r'^payudantias/',payudantias),
    url(r'^pequipo/', pequipo),
    url(r'^pnoticias/',pnoticias),
    url(r'^pranking/',pranking),
    url(r'^payudantesa/',payudantesa),
    url(r'^payudantesd/',payudantesd),
    url(r'^pcoordinador/',pcoordinador)
    
   
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)