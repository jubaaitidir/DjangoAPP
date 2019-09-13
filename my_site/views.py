from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm,LoginForm, RegisterForm
from .config import our_insert_many,db, get_Sales, get_Sale
from .logic_for_views import get_graph_data
import pymongo
import pprint

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
        items={'titre':"chaise",'ref':"chaise_table_xl"}
        print(request.POST["message"])
    return render(request, 'contact.html',locals())



def login(request):
    form_ins= LoginForm(request.POST or None)
    if form_ins.is_valid():
        email=form_ins.cleaned_data["email"]
        pwd=form_ins.cleaned_data["pwd"]
        envoi_ins=True
        print(request.POST["pwd"])
    return render(request,"login.html",locals())

def register(request):
    form_register= RegisterForm(request.POST or None)
    if form_register.is_valid():
        nom=form_register.cleaned_data["nom"]
        prenom=form_register.cleaned_data["prenom"]
        email=form_register.cleaned_data["email"]
        pwd=form_register.cleaned_data["pwd"]
        repeat_pwd=form_register.cleaned_data["repeat_pwd"]
        envoi_register=True
        print(request.POST["pwd"])
    return render(request,"register.html",locals())


def show_image(request):
    """
    Une vue qui renvoie une réponse HTTP contenant le graph généré.
    """
    data = get_graph_data()
    return HttpResponse(data, content_type="image/png")


def profile(request):
    print('user == ',request.user)
    print('is_authenticated ',request.user.is_authenticated)
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return redirect('/accounts/login')

def mesFactures(request):
    print('user = ', request.user)
    sales = get_Sales(request.user.username)
    new_sales = list(sales)
    for s in new_sales:
        s['id'] = s['_id']
    print('sales ===== ', list(new_sales))
    return render(request, 'mesfactures.html', {'factures': new_sales})

def facture(request, ref_facture):
    # list_product = get_all_products()
    sale_obj = get_Sale(request.user.username, ref_facture)
    # if len(list_product) == 0:
    #     list_product = []
    subtotal=0
    shipping=0
    total=0
    # for s in get_Sale():
    #     print(s)
    for s in get_Sale(request.user.username, ref_facture):
        subtotal += s['product']['pu'] * s['quantity']
        shipping += s['shipping']
        total += subtotal
    
    return render(request, "facture.html", {'sale': sale_obj, 'subtotal': subtotal, 'shipping': shipping, 'total': total})