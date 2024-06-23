
from ast import arg
from django.urls import reverse
from django.shortcuts import redirect, render
from django.views import View
from django.http import JsonResponse
from .models import *
from follower.models import *
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.contrib.auth import authenticate,login,logout

from django.contrib import messages

# Create your views here.


class IndexPageView(View):
    def get(self, request):
        categorys = Category.objects.all()
        
        articles = Article.objects.all().order_by('likes')[:10]
        fallowers = Fallower.objects.all().order_by('rating')[:10]
        
        context = {"categorys":categorys,"articles":articles,"fallowers":fallowers}
        
        return render(request, "index.html", context)


class DetailPageView(View):
    def get(self,request,article_id):
        fallower = None
        try:
            user = request.user
            if isinstance(user, User):
                fallower = Fallower.objects.get(user=user)
        except Fallower.DoesNotExist as error:
            fallower = None
       
        print(fallower)
       
        article = Article.objects.get(id=article_id)
        
        comments = article.comments.all().order_by('-id')[:10]
       
        comments2 = Comment.objects.filter(article=article)

        categorys = Category.objects.all()

        articles = Article.objects.all().order_by('likes')[:10]
        fallowers = Fallower.objects.all().order_by('rating')[:10]
        context = {"categorys":categorys,"articles":articles,"fallowers":fallowers}
        
        context["article"] = article
        context["fallower"] = fallower
        context["comments"] = comments
        return render(request,"detail.html",context )


class AuthorArticlesView(ListView):
    template_name = "index.html"
    # queryset =  Article.objects.all().order_by('likes')
    context_object_name = "articles"

    def get_queryset(self):
        author_id = self.kwargs.get("pk")
        fallower = Fallower.objects.get(id=int(author_id))
        return Article.objects.filter(author=fallower).order_by('likes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorys'] =  Category.objects.all()
        context['fallowers'] =  Fallower.objects.all().order_by('rating')[:10]
        return context


class LoginView(View):
    def get(self,request):
        return render(request, "login.html")

    def post(self,request):
        username = request.POST['username']    
        password = request.POST['password']
        check = User.objects.filter(username=username).exists()
        if check:
            user  = User.objects.get(username=username)   
            user = authenticate(request,username=username,password=password)
            if user:
                    login(request,user)
                    messages.add_message(request, messages.SUCCESS,"Avtorizatsiya muvaffaqiyatli yakunlandi !")
                    return redirect("blog:home_page")
            else:
                messages.add_message(request, messages.WARNING,"Parol noto'g'ri !")

        else:
            messages.add_message(request, messages.WARNING,"Bunday user mavjud emas !")

        return redirect("blog:login")  


def reaction(request):
    reaction_type = request.GET['target']
    a_id = request.GET['article_id']
    article = Article.objects.get(id=int(a_id))
    user = request.user
    fallower = Fallower.objects.get(user=user)
    if article not in fallower.liked_articles.all():
        if reaction_type == "likes":
            article.likes += 1
        else:    
            article.dislikes += 1
        article.save()
        fallower.liked_articles.add(article)
        # fallower.liked_articles.remove(article)
        # fallower.liked_articles.clear()
        # fallower.liked_articles.get(id=5)
        # fallower.liked_articles.create()
        # fallower.liked_articles.all()
        # fallower.liked_articles.filter(name="Ajoyib maqola")
    response = {"likes":article.likes,"dislikes":article.dislikes}
    return JsonResponse(response)

class CategoryView(View):
    
    def get(self,request,category_id):
        category = Category.objects.get(id=category_id)
        categorys = Category.objects.all()
        articles = Article.objects.all().order_by('likes')[:10]
        articles = Article.objects.filter(category=category)
        fallowers = Fallower.objects.all().order_by('rating')[:10]
        context = {"categorys":categorys,"articles":articles,"fallowers":fallowers}
        return render(request,"index.html",context)  

def add_comment(request):
    print(request.POST)
    comment = request.POST['comment']
    article_id = request.POST['article_id']
    a = Article.objects.get(id=int(article_id))
    user = request.user
    fallower = Fallower.objects.get(user=user)
    Comment.objects.create(article=a,author=fallower,text=comment)
    url = reverse("blog:detail", kwargs={"article_id":article_id})
    print(url)
    return redirect(url)
