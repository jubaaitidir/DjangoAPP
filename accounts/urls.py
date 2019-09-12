from django.urls import path
from django.contrib.auth import views as auth_views
from my_site.views import login,register,profile
from django.views.generic.edit import CreateView
# from django.contrib.auth.forms import UserCreationForm
from my_site.register_model import UserCreateForm

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(),name='login'),
    # path('register/',register,name='register'),
    path('register/', CreateView.as_view(template_name='register.html',form_class=UserCreateForm,success_url='/')),
    # path('password-reset/', views.PasswordResetView.as_view(), name='password_reset'),
    # path('password-reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('profile/',profile,name='profile'),
]