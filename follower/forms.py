from distutils.log import error
from email.policy import default
from attr import attr
from django import  forms
from .models import Fallower


class AddFallowerForm(forms.Form):
    username = forms.CharField(max_length=15,label="Username",
        widget=forms.widgets.TextInput(
                attrs={"class":"form-control"}
            ))

    password = forms.CharField(max_length=15,label="Password",
          widget=forms.widgets.PasswordInput(
                attrs={"class":"form-control"}
            ))

    password_confirm = forms.CharField(max_length=15,label="Password confirm",
        widget=forms.widgets.PasswordInput(
                attrs={"class":"form-control"}
            ))
    name = forms.CharField(max_length=15,label="Name",
     widget=forms.widgets.TextInput(
                attrs={"class":"form-control"}
            ))
    surname = forms.CharField(max_length=15,label="Surname",
     widget=forms.widgets.TextInput(
                attrs={"class":"form-control"}
            ))
    age = forms.IntegerField(label="Age",
     widget=forms.widgets.NumberInput(
                attrs={"class":"form-control"}
            ))
    adress = forms.CharField(max_length=150,label="Adress",
     widget=forms.widgets.TextInput(
                attrs={"class":"form-control"}
            ))
    email = forms.EmailField(max_length=30,label="Email",
     widget=forms.widgets.EmailInput(
                attrs={"class":"form-control"}
            ))

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 8:
            raise forms.ValidationError("Username 8 ta belgidan kam bo'lmasin")
        return username    

    # def clean_password_confirm(self):
    #     print( self.cleaned_data)
    #     password_confirm = self.cleaned_data['password_confirm']
    #     if len(password_confirm) < 8:
    #         raise forms.ValidationError("Parol 8 ta belgidan kam bo'lmasin")
    #     return password_confirm    

   
    def clean(self):
        super().clean()
        print( self.cleaned_data)
        errors = {}
        password = self.cleaned_data['password']
        password_confirm = self.cleaned_data['password_confirm']
        if password != password_confirm:
            errors['password_confirm'] = forms.ValidationError("Parollar bir xil emas")
        if self.cleaned_data['age'] < 18:
            errors['age'] = forms.ValidationError("Yoshingiz mos kelmadi")
        if errors:
            raise forms.ValidationError(errors)
    
    def save(self, *args, **kwargs):
        print(self)
        print(args)
        print(kwargs)

    #     model = Fallower
    #     fields = ("user","name","surname",'age','email',"adress")




    