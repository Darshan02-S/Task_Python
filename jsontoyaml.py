import requests
import yaml

def jsontoyaml(file):
    r = requests.get('https://randomuser.me/api/?results=5') #statuscode<200>

    data = r.json() #gets data in json format from responce

    file_open = open(file, "w") #file is opened with write method
    yaml.dump(data, file_open) #yaml.dump is used convert the json data to yaml

    file_open.close()#file will close
jsontoyaml("darshan.yaml")
