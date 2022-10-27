from flask import Flask
from requests import get
import requests 

app = Flask(__name__)
response = get('https://ipapi.co/json/').json()

# IP Address (IPv4)
@app.route('/ip', methods = ['GET'])
def get_ip():
    return {'IP Address': response['ip']}

# ASN
@app.route('/asn', methods = ['GET'])
def get_asn():
        return {'ASN' : response['asn']}


# CountryCode
@app.route('/countrycode', methods = ['GET'])
def get_countryCode():
    response = get('https://ipapi.co/json/').json()
    return {'Country' : response['country_code']}

# Geolocation
@app.route('/geoloc', methods = ['GET'])
def get_myip():
        response = get('https://api64.ipify.org?format=json').json()
        return response["ip"]
def get_geoloc():
        ip_address = get_myip()
        response =  get(f'https://ipapi.co/{ip_address}/json/').json()
        location_data = {
            "country": response.get("country_name"),
            "continent_code": response.get("continent_code"),
            "region": response.get("region"),
            "country_capital": response.get("country_capital"),
            "city": response.get("city"),
            "latitude": response.get("latitude"),
            "longitude": response.get("longitude")
        }
        # return {'Country' : response['country_name'], 
        # "continent_code": response["continent_code"],
        # "region": response["region"]}
        return location_data


if __name__ == "__main__":
    app.run()
