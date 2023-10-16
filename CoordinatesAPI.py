import requests
import sys

#References: 
# https://ipstack.com/blog/using-python-to-convert-ip-addresses-into-location-data
# https://ipstack.com/documentation
# https://medium.com/geekculture/how-to-dockerize-a-python-script-b0af3cd11fb0


def getCoordinates(ip_address, api_key):
    base_url = "http://api.ipstack.com/"
    response = requests.get(f"{base_url}{ip_address}?access_key={api_key}&fields={'latitude,longitude'}")
    data = response.json() #data is returned as a dictionary
    latitude = data["latitude"]
    longitude = data["longitude"]
    return latitude, longitude  # Returns the lat and long as a tuple of Strings

apiAccessKey = "61f6673544e69512bafda6c994bfd715" 
userIP = sys.argv[1] #IP for now #66.45.44.0 Random Colorado IP
output = getCoordinates(userIP, apiAccessKey)
print(output) # output is a tuple of Strings
