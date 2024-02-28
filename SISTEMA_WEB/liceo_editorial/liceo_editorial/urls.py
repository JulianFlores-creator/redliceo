
from django.contrib import admin
from django.urls import path, re_path

from contacto_info.views import contacto
from galeria_eventos.views import event_list, event_detail
from home.views import informacion, lineaGeneralConocimiento, about_page
from instituciones_colaboradoras.views import subir_foto, mostrar_foto
from memorias_red_liceo.views import capturarMemoria, mostrarMemorias, verMemorias
from miembros.views import miembrosRedLiceo
from recursos.views import subir_recurso, lista_recursos, ver_pdf

#Importaciones para tratamiento de fotos
#Recuerda configurar settings
from django.conf import settings
from django .views.static import serve



urlpatterns = [

    path('admin/', admin.site.urls),
    path('', informacion, name='informacion'),
    path('subir/', subir_recurso, name='subir_recurso'),
    path('media/recursos/', lista_recursos, name='lista_recursos'),
    path('lineaGC/',lineaGeneralConocimiento, name='lineaGC'),
    path('about/', about_page, name='about'),
    path('miembros/', miembrosRedLiceo, name="miembrosRedLiceo"),
    path('contacto/', contacto, name='pagina_contacto'),
    path('subirFoto', subir_foto, name="subirFoto"),
    path('mostrarFoto', mostrar_foto, name="mostrarFoto"),
    path('listarEvento/',event_list, name='listarEvento'),
    path('listarEvento/detalleEvento/<int:event_id>/',event_detail, name='detalleEvento'),
    path('capturar-memoria/', capturarMemoria, name='capturar_documento'),
    path('media/memorias_red_liceo/', mostrarMemorias, name='media/memorias_red_liceo'),
    path('encuentros/<int:m_id>/',verMemorias,name='encuentros')
]

#Configuracion, para mostrar fotos
urlpatterns +=[
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    })
]