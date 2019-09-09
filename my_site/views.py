from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm

def home_page_view(request):
    return HttpResponse("Hello world !")

def home_page_view_with_render(request):
    return render(request,"index.html")


def contact(request):
    form= ContactForm(request.POST or None)
    if form.is_valid():
        sujet=form.cleaned_data["sujet"]
        message=form.cleaned_data["message"]
        envoyeur=form.cleaned_data["envoyeur"]
        renvoi=form.cleaned_data["renvoi"]
        envoi=True
    return render(request, 'contact.html',locals())