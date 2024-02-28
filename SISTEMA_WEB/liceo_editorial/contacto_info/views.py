from django.shortcuts import render, redirect

from contacto_info.form import ContactoForm

from django.core.mail import send_mail
from django.conf import settings

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('informacion')


    else:
        form = ContactoForm()
    return render(request, 'contacto.html', {'form': form})
