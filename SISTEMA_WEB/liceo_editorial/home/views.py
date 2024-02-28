from django.shortcuts import render


from .models import Informacion, LGC, AboutInfo


def informacion(request):
    informacion = Informacion.objects.all()
    return render(request, 'informacion.html', {'informacion': informacion})


# noinspection PyUnresolvedReferences
def lineaGeneralConocimiento(request):
    linea = LGC.objects.all()
    return render(request,'lgc.html', {'lgc':linea} )

def about_page(request):
    informacion = AboutInfo.objects.all()
    return render(request, 'about.html', {'info':informacion})



