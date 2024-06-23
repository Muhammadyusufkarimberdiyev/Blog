from sre_constants import SUCCESS
from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from .forms import AddFallowerForm
from django.contrib import messages
# Create your views here.

class RegisterView(View):
    def get(self,request):
        form = AddFallowerForm()
        context = {'form':form}
        return render(request, "register.html" ,context)

    def post(self,request):
        form = AddFallowerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"Registratsiya muvaffaqiyatli yakunlandi")
            return redirect("blog:login")
        print( form.errors )    
        context = {'form':form}
        return render(request, "register.html" ,context)    

class ProfilView(View):
    def get(self,request):
        return render(request,"profil.html")