from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from .models import Post

class SinUpForm(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput())
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email'}
    widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
             'first_name':forms.TextInput(attrs={'class':'form-control'}),
             'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
             }
        
        
        
class LoginForm(AuthenticationForm):
     username=UsernameField(widget=forms.TimeInput(attrs={'autofocus':True,'class':'form-control'}))
     #password=forms.CharField(label='Password',widget=forms.PasswordInput())

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'
        labels={'title:Title','desc:Description'}
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'desc':forms.Textarea(attrs={'class':'form-control'}),
        }
        