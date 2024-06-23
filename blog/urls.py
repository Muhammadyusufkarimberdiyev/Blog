from django.urls import path
from .views import *

app_name = "blog"

urlpatterns = [
    
    path("", IndexPageView.as_view(), name="home_page"),
    path("<int:article_id>", DetailPageView.as_view(), name="detail"),
    path("reaction", reaction, name="reaction"),
    path("category/<int:category_id>", CategoryView.as_view(), name="category"),
    path("add_comment", add_comment, name="add_comment"),
    path("author/<int:pk>/articles", AuthorArticlesView.as_view(), name="author_articles"),
    path("login", LoginView.as_view(), name="login"),
]
