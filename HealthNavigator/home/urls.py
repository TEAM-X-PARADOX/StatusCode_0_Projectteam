from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path("",views.index,name="Home"),
    path("about",views.about,name="About"),
    path("services",views.services,name="Services"),
    path("contact",views.contact,name="Contact"),
    path("consult",views.consult,name="consult"),
    path("check",views.check,name="check"),
    path("signup",views.Usersignup,name="Usersignup"),
    path("login",views.Userlogin,name="Userlogin"),
    path("logout",views.Userlogout,name="Userlogout"),
]