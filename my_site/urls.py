"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from django.contrib.auth import views as auth_views
from .views import home_page_view,home_page_view_with_render,contact,login,register
from django.views.generic.edit import CreateView
# from django.contrib.auth.forms import UserCreationForm
from .register_model import UserCreateForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_page_view_with_render,name='home_default_page_render'),
    path('home/',home_page_view_with_render,name='home_page_render'),
    path('contact/',contact,name='contact'),
    # path('login/',login,name='login'),
    # path('login/',auth_views.LoginView.as_view(),name='login'),
    # path('register/',register,name='register'),
    # path('register/', CreateView.as_view(template_name='register.html',form_class=UserCreateForm,success_url='/')),
    path('accounts/',include("accounts.urls"))
]
