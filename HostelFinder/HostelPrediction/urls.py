from django.urls import path
from . import views
urlpatterns = [
    path("HostelPrediction",views.HostelPrediction,name="hostelPrediction"),
    path("HostelRecom",views.HostelRecom,name="HostelRecom")
]
