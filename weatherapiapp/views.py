from django.shortcuts import render
from rest_framework import viewsets
from .models import guest
from .serializer import GuestSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
from django.conf import settings
from .my_weather_scraper.weather import run_script
import os
# Create your views here.



class GuestViewset(viewsets.ModelViewSet):
    """
    default : it will show all guests \n
    update/delete : guest/id will return guest details belong to id (eg:1)\n\n
    Methods \n
        \t\tPOST :    Create guest
        \t\tGET :     Get all guests
        \t\tPUT :     Update guest by id
        \t\tDELETE :  Delete guest by id
    """
    queryset = guest.objects.all()
    serializer_class = GuestSerializer

@api_view(['GET'])
def weatherapi(request):
    
    if run_script():
        dataframe = pd.read_csv(os.path.join(settings.BASE_DIR,"weatherapiapp","my_weather_scraper","weather.csv"),index_col=False)
        result =  dataframe.to_dict('list')
        status_code = status.HTTP_200_OK
    else:
        result = 'Script failed to run'
        status_code = status.HTTP_400_BAD_REQUEST
    return Response({"data":result},status=status_code)