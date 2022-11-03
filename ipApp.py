from flask import Flask, request, render_template
from requests import get
import requests 
import ipapi


app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def Index():
    search = request.form.get('search')
    data = ipapi.location(ip=search, output='json')
    return render_template('index.html', data=data)

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
        return {'ASN' : response.get('asn')}

# ISP
@app.route('/isp', methods = ['GET'])
def get_isp():
    return {'ISP': response.get('org')}

# CountryCode
@app.route('/countrycode', methods = ['GET'])
def get_countryCode():
    return {'Country Code' : response.get('country_code')}

# Geolocation
@app.route('/geoloc', methods = ['GET'])
def get_geoloc():
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
@app.route('/ipapp', methods = ['GET'])
def get_all():
    data = {
        'IP Address (IPv4)': response.get('ip'),
        'ASN' : response.get('asn'),
        'ISP' : response.get('org'),
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