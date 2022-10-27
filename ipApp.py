from flask import Flask
from requests import get
import requests 

app = Flask(__name__)

# IP Address (IPv4)
@app.route('/ip', methods = ['GET'])
def get_ip():
    # return {'IP Address (IPv4)': apiResponse['ip']}
    ip_api = requests.get('https://ipapi.co/json/').json()
    return ip_api['ip']
    
ip_address = get_ip()
response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()


# ASN
@app.route('/asn', methods = ['GET'])
def get_asn():
        return {'ASN' : apiResponse['asn']}


# CountryCode
@app.route('/countrycode', methods = ['GET'])
def get_countryCode():
    return {'Country Code' : apiResponse['country_code']}

# Geolocation
# def get_ip():
#     response = requests.get('https://api64.ipify.org?format=json').json()
#     return response["ip"]
@app.route('/geoloc', methods = ['GET'])
def get_geoloc():
    # ip_address = get_ip()
    # response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "Country": response.get("country_name"),
        "Continent_code": response.get("continent_code"),
        "Region": response.get("region"),
        "Country_capital": response.get("country_capital"),
        "City": response.get("city"),
        "Latitude": response.get("latitude"),
        "Longitude": response.get("longitude")
    }
    return location_data

# All
@app.route('/ipApp', methods = ['GET'])
def get_all():
    # ip_address = get_ip()
    # response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    data = {
        'IP Address (IPv4)': response.get('ip'),
        'ASN' : response.get('asn'),
        'Country Code' : response.get('country_code'),
        "Country": response.get("country_name"),
        "Continent_code": response.get("continent_code"),
        "Region": response.get("region"),
        "Country_capital": response.get("country_capital"),
        "City": response.get("city"),
        "Latitude": response.get("latitude"),
        "Longitude": response.get("longitude")
    }
    return data


if __name__ == "__main__":
    app.run()
