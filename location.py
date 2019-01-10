import sys
import requests

def get_location():
    url = "http://ipinfo.io"
    response = requests.get(url)
    location = response.json()['loc']
    return location

def get_address(latitude,longitude):
    url = "https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat="+latitude+"&lon="+longitude
    response = requests.get(url)
    address = response.json()["display_name"]
    return "Your address is  : {}".format(address)


if len(sys.argv) <2 :
    [lat,long] = get_location().split(",")
    print(get_address(lat,long))

elif len(sys.argv) >=3 :
    [lat,long] = [sys.argv[1],sys.argv[2]]
    print(get_address(lat,long))
