import requests
import json

api_key = "7e36055b8140e40cc554d26815300eaa" #its a default API generated as we signin the openweatherapi website
url = "https://api.openweathermap.org/data/2.5/weather" #opensource API
def openweatherapi(location):
    r = requests.get('{}?q={}&appid={}&units=metric'.format(url, location, api_key)) #formating the api with location and apikey
    data = json.loads(r.text) #get the datas as json format from the API and.text is used to say that the json objects are in string format
    print('City : ', data['name'])
    print('Description : ', data['weather'][0]['description'])
    print('Temperature : ', data['main']['temp'])
    print('Temperature : ', data['main']['temp'])
    print('Latitude, Longitude : ', data['coord']['lon'], ',', data['coord']['lat'])
    print('Pressure : ', data['main']['pressure'])
    print('Humidity : ', data['main']['humidity'])
    print('Wind Speed : ', data['wind']['speed'])
    #these are the needed datas from the json
location = input("enter location : ")
openweatherapi(location)
