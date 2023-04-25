from django.urls import path
from . import views
urlpatterns = [
    path("pricePrediction",views.pricePrediction,name="pricePrediction"),
    path("result",views.result,name="result")
    
]
