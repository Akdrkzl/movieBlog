from django import forms
from django.forms import widgets

from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User
from .models import CustomUser


class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control form-control-user','id':'exampleInputEmail','aria-describedby':'emailHelp','placeholder':'Enter Email Address...'}))
    password =forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-user','id':'exampleInputPassword','placeholder':'Password'}))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not CustomUser.objects.filter(email = email).exists():
            self.add_error('email','Bu Mail Adresi Kayıtlı Değil')
        return email
    

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','email')
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['first_name'].widget = widgets.TextInput(attrs={'class':'form-control form-control-user','id':'exampleFirstName','placeholder':'First Name'})
        self.fields['last_name'].widget = widgets.TextInput(attrs={'class':'form-control form-control-user','id':'exampleLastName','placeholder':'Last Name'})
        self.fields['email'].widget = widgets.EmailInput(attrs={'class':'form-control form-control-user','id':'exampleInputEmail','placeholder':'Email Address'})
        self.fields['password1'].widget = widgets.PasswordInput(attrs={'class':'form-control form-control-user','id':'exampleInputPassword','placeholder':'Password'})
        self.fields['password2'].widget = widgets.PasswordInput(attrs={'class':'form-control form-control-user','id':'exampleRepeatPassword','placeholder':'Password Repeat'})
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if CustomUser.objects.filter(email = email).exists():
            self.add_error('email','Bu mail adresi kullanılıyor')
        
        return email
    
class UserUpdate(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','email','user_photo','state','city','zip','tel')
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['first_name'].widget = widgets.TextInput(attrs={'class':'form-control','placeholder':'First Name'})
        self.fields['last_name'].widget = widgets.TextInput(attrs={'class':'form-control','placeholder':'Last Name'})
        self.fields['email'].widget = widgets.TextInput(attrs={'class':'form-control','placeholder':'Email Address'})
        self.fields['user_photo'].widget = widgets.FileInput(attrs={'class':'form-control p-0 h-100 w-50'})
        self.fields['state'].widget = widgets.TextInput(attrs={'class':'form-control','placeholder':'State'})
        self.fields['city'].widget = widgets.TextInput(attrs={'class':'form-control','placeholder':'City'})
        self.fields['zip'].widget = widgets.NumberInput(attrs={'class':'form-control','placeholder':'Zip Code'})
        self.fields['tel'].widget = widgets.TextInput(attrs={'class':'form-control','placeholder':'Phone'})