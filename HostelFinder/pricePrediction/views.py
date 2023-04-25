from django.shortcuts import render,HttpResponse
from joblib import load
from json import JSONEncoder
import json
import numpy

model=load("./savedmodels/model.joblib")

# Create your views here.
def pricePrediction(request):
    

    return render(request,"pricePrediction.html")
def result(request):
    if request.method=="POST":
            bed=request.POST.get("beds")
            food=request.POST.get("food")
            ac=request.POST.get("ac")
            laundry=request.POST.get("laundry")
            security=request.POST.get("security")
            rating=request.POST.get("rating")
            
            y_pred=model.predict([[int(bed),int(ac),int(security),int(food),float(rating),int(laundry)]])
            
            return render(request,"result.html",{"result":(y_pred[0])})

    
    