from django.urls import path
from .views import *


app_name = "follower"

urlpatterns = [
    path("registration", RegisterView.as_view(), name = "register"),
    path("profil", ProfilView.as_view(), name = "profil")
]
