"""HostelFinder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app1 import views as v1
from pricePrediction import views
from HostelPrediction import views as v2
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",v1.SignupPage,name="signup"),
    path("login/",v1.LoginPage,name="login"),
    path("home/",v1.HomePage,name="home"),
    path("pricePrediction/",views.pricePrediction,name="pricePrediction"),
    path("pricePrediction/result",views.result,name="result"),
    path("logout/",v1.LogoutPage,name="logout"),
    path("HostelPrediction",v2.HostelPrediction,name="hostelPrediction"),
    path("HostelRecom",v2.HostelRecom,name="HostelRecom"),
    
]
