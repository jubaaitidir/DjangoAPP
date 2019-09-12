from django import forms


class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    envoyeur = forms.EmailField(label="Votre adresse e-mail")
    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)


class LoginForm(forms.Form):
    email= forms.EmailField(max_length=30)
    pwd= forms.CharField(max_length=20, widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    nom = forms.CharField(max_length=30)
    prenom = forms.CharField(max_length=30)
    datenais = forms.DateField(label= "date naissance", required=True)
    email= forms.EmailField(max_length=30)
    pwd= forms.CharField(max_length=20, widget=forms.PasswordInput)
    nom.widget.attrs.update({'class':'form-control'})
    prenom.widget.attrs.update({'class':'form-control'})
    datenais.widget.attrs.update({'class':'form-control'})
    email.widget.attrs.update({'class':'form-control'})
    pwd.widget.attrs.update({'class':'form-control '})

    repeat_pwd= forms.CharField(max_length=20, widget=forms.PasswordInput)
    