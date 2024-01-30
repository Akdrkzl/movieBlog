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
    

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
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

        if User.objects.filter(email = email).exists():
            self.add_error('email','Bu mail adresi kullanılıyor')
        
        return email