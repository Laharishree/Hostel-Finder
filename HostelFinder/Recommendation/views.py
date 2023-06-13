from django.shortcuts import render
from .NLPRecom import recommend_hotel
from django.http import JsonResponse
import json
# Create your views here.
def Recommendation(requests):

    return render(requests,"recommendation.html")

def NLPResult(requests):
    if requests.method == 'POST':
        request = requests.POST
        locality=request.get("locality")
        desc=request.get("Description")
        result=recommend_hotel(locality,desc)
        result_dict = result.to_dict('records')
        print(locality)
        print(desc)
        # Hostel=JsonResponse(result_dict, safe=False)

        return render(requests, "NLPResult.html", {"result1": result_dict})
    

        

