from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User
from django.forms import widgets


class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control form-control-user','id':'exampleInputEmail','aria-describedby':'emailHelp','placeholder':'Enter Email Address...'}))
    password =forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-user','id':'exampleInputPassword','placeholder':'Password'}))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email = email).exists():
            self.add_error('email','Bu Mail Adresi Kayıtlı Değil')
        return email