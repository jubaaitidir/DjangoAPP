from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.forms import User
from django.contrib.auth.models import User
# from .models import Profile
import datetime

STATES = (
    ('', 'Choose...'),
    ('FR', 'France'),
    ('SU', 'Suisse'),
    ('SP', 'Espagne'),
    ('USA', 'Etats-Unis'),
    ('CH', 'Chine '),
    ('IT', 'Italie'),
    ('GB', 'Royaume-Uni'),
    ('DE', 'Allemagne'),
    ('TU', 'Turquie'),
    ('MA', 'Maroc'),
)
class UserCreateForm(UserCreationForm):
    error_messages = {
        'password_mismatch': "Les deux champs de mot de passe ne correspondent pas.",
    }

    email = forms.EmailField(required=True,label='Email',error_messages={'exists': 'Oops'}, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='Login',widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Mot de Passe',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirmer votre mot de passe',widget=forms.PasswordInput(attrs={'class': 'form-control'}))#,help_text="Enter the same password as above, for verification.")
    # 'address': {'nbr': 84, 'street': 'rue Tabakayo', 'apprt': '' ,'zib_code': 95684, 'city': 'Chinta', 'country':'Dreamland'}
    firstname = forms.CharField(required=True,label='Prénom', widget=forms.TextInput(attrs={'class': 'form-control'}))
    lastname = forms.CharField(required=True,label='Nom', widget=forms.TextInput(attrs={'class': 'form-control'}))
    birth_date = forms.DateField(initial=datetime.date.today,label='La date de naissance', widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    account_type = forms.TypedChoiceField(
                   coerce=lambda x: x == 'True',
                   choices=((False, 'Normal'), (True, 'Entreprise')),
                   widget=forms.RadioSelect,
                   label='le type de votre compte :'
                )
    address_nbr = forms.CharField(required=True,label='N', widget=forms.TextInput(attrs={'class': 'form-control'}))
    address_street = forms.CharField(required=True,label='Rue/Boulevard...', widget=forms.TextInput(attrs={'class': 'form-control'}))
    address_apprt = forms.CharField(required=False,label='Appart...', widget=forms.TextInput(attrs={'class': 'form-control'}))
    address_zib_code = forms.CharField(required=True,label='Code postale', widget=forms.TextInput(attrs={'class': 'form-control'}))
    address_city = forms.CharField(required=True,label='Ville', widget=forms.TextInput(attrs={'class': 'form-control'}))
    address_country = forms.ChoiceField(choices=STATES,required=True,label='Pays', widget=forms.Select(attrs={'class': 'form-control'}))
    # address_country = forms.CharField(required=True,label='Pays', widget=forms.TextInput(attrs={'class': 'form-control'}))


    class Meta:
        model = User
        # model = Profile
        fields = ("firstname","lastname","username", "birth_date","email", "password1", "password2","account_type","address_nbr","address_street","address_apprt","address_zib_code","address_city","address_country")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.profile.firstname = self.cleaned_data["firstname"]
        user.profile.lastname = self.cleaned_data["lastname"]
        user.profile.birth_date = self.cleaned_data["birth_date"]
        user.profile.account_type = self.cleaned_data["email"]
        
        adresse = {'nbr':self.cleaned_data["address_nbr"], 'street':self.cleaned_data["address_street"], 'apprt': self.cleaned_data["address_apprt"],'zib_code': self.cleaned_data["address_zib_code"], 'city': self.cleaned_data["address_city"], 'country':self.cleaned_data["address_city"]}
        user.address = adresse
        # user.address_nbr = self.cleaned_data["address_nbr"]
        # user.address_street = self.cleaned_data["address_street"]
        # user.address_apprt = self.cleaned_data["address_apprt"]
        # user.address_zib_code = self.cleaned_data["address_zib_code"]
        # user.address_city = self.cleaned_data["address_city"]
        # user.address_country = self.cleaned_data["address_country"]
        
        if commit:
            print('saved user = ', user)
            user.save()
        return user

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError(self.fields['email'].error_messages['exists'])
        return self.cleaned_data['email']