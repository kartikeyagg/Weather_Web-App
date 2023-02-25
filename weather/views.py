from django.shortcuts import render
import json
import urllib.request
# Create your views here.

# the below code stats that if the method of calling it is post
# which means it is called by another page instead of directly 
# entering the url 
# than it should perform ohter things
# else render the index.html page directly

def index(request):

    if request.method == 'POST':

        city = request.POST['city']

        apikey = '6e5c241ac3484d61a0d83137231902'

        res = urllib.request.urlopen('https://api.weatherapi.com/v1/current.json?key='+str(apikey)+'&q='+str(city))

        json_data = json.load(res)

        data = {
            "Location name": str(json_data['location']['name']),
            "coordinates": str(str(json_data['location']['lat']) +str(" deg , ") +str(json_data['location']['lon'] ) +" deg" ),
            'temp': str(json_data['current']['temp_c']) +" deg C",
            'pressure': str(json_data['current']['pressure_mb']) +str(" mb"),
            'humidity': str(json_data['current']['humidity']),
        }
        
       

        param = {

            'city':city,
            'data':data, 

        }



    else :
        param = {'city':'',}


    return render(request, 'index.html',param)
