from django.shortcuts import render,HttpResponse
from joblib import load
import numpy
import pandas as pd
from geopy.geocoders import Nominatim
location_Connection=Nominatim(user_agent="geoapiExercise")


import json


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from .recommendation import recommend_hostels
# Create your views here.
def HostelPrediction(request):

    return render(request,"HostelPrediction.html")
def HostelRecom(request):
    if request.method == 'POST':
        data = request.POST
        # latitude = float(data.get('latitude'))
        # longitude = float(data.get('longitude'))
        location=data.get("Location")
        grid=location_Connection.geocode(location)
        latitude=grid.latitude
        longitude=grid.longitude

        price = int(data.get('price'))
        wifi = int(data.get('wifi'))
        ac = int(data.get('ac'))
        laundry = int(data.get('laundry'))
        security = int(data.get('security'))
        rating = float(data.get('rating'))
        
        recommended_hostels = recommend_hostels(latitude, longitude, price, wifi, ac, laundry, security, rating)
        recommended_hostels = recommended_hostels[['Hostel_name', 'price', 'Rating','latitude','longitude',"BusStop","Distance"]]
        Hostel = recommended_hostels.to_dict(orient='records')
        
        hostelsData=json.dumps(Hostel,indent=2)
        
        with open("HostelFinder/static/mydata.json", "w") as final:
            final.write(hostelsData)
         
                

        return render(request,"HostelResult.html",{"data":Hostel})
        # JsonResponse({'hostels': recommended_hostels})


        
        

     