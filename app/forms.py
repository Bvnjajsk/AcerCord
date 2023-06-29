from django import forms
from .models import Contacto,Producto
from django.contrib.auth.forms import UserCreationForm


class ContactoForm(forms.ModelForm):

    nombre   = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    correo   = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))


    class Meta:
        model  = Contacto
        fields ='__all__'



class ProductoForm(forms.ModelForm):
    class Meta:
        model =Producto
        fields ='__all__'





class CustomUserCreationForm(UserCreationForm):
    pass