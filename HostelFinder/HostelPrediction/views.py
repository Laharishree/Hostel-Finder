from django.shortcuts import render,HttpResponse
from joblib import load
import numpy
import pandas as pd
from geopy.geocoders import Nominatim
from django.shortcuts import render
from selenium import webdriver
import folium
from bs4 import BeautifulSoup as BS

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
        print(latitude, longitude, price, wifi, ac, laundry, security, rating)
        
        recommended_hostels = recommend_hostels(latitude, longitude, price, wifi, ac, laundry, security, rating)
        recommended_hostels = recommended_hostels[['Hostel_name',"address", 'price', 'Rating','latitude','longitude',"BusStop","Distance","EmbeddedMap"]]
        Hostel = recommended_hostels.to_dict(orient='records')

        



        map_center = [latitude,longitude]
        map_zoom = 12
        map_obj = folium.Map(location=map_center, zoom_start=map_zoom)
        for i in Hostel:
            folium.Marker([i.get("latitude"),i.get("longitude")],popup =i.get("Hostel_name")).add_to(map_obj)
        
        map_obj.save("E:/Hostel-Finder/HostelFinder/templates/HostelResultFinal.html")

        
        # Example usage
        to =data.get("email")
        subject = 'Hostel/PG Recommendation'
        body = ""
        for i in Hostel:
            body+="Hostel Name:"
            body+=i["Hostel_name"]+"\n"
            body+="Price:"
            body+="\n"+str(i["price"])+"\n"
            body+="Rating"
            body+="\n"+str(i["Rating"])+"\n"
            body+="view on map: "
            body+=i["EmbeddedMap"]
            body+="\n\n"
        send_email(to,subject,body)
        
    
        
        
         
                

    return render(request,"HostelResult.html",{"data":Hostel,})
        # JsonResponse({'hostels': recommended_hostels})
import smtplib

def send_email(to, subject, body):
    # Set up the connection to the email server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('hostelfinder2023@gmail.com', 'gvppampqnvbgjgow')

    # Create the email message
    message = f"Subject: {subject}\n\n{body}"

    # Send the email
    server.sendmail('hostelfinder2023@gmail.com', to, message)

    # Close the connection to the email server
    server.quit()

def MapDirect(request):
        return render(request,"HostelResultFinal.html")




        
        

     