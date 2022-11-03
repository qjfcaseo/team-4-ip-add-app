from flask import Flask, request, render_template
from requests import get
import requests 
import ipapi


app = Flask(__name__)



# IP Address (IPv4)
@app.route('/ip', methods = ['GET'])
def get_ip():
    # return {'IP Address (IPv4)': apiResponse['ip']}
    ip_api = requests.get('https://ipapi.co/json/?key=V27xzP081ObqkaS8qJvRDHq8DEFMoULOKsqVhBcZkw0rYwBH0Q').json()
    return ip_api['ip']

ip_address = get_ip()
response = requests.get(f'https://ipapi.co/{ip_address}/json/?key=V27xzP081ObqkaS8qJvRDHq8DEFMoULOKsqVhBcZkw0rYwBH0Q').json()


@app.route('/', methods = ['GET', 'POST'])
def Index():
    search = request.form.get('search')
    while search == None:
    # data = ipapi.location(ip=search, output='json')
        data = response
    else:
        data = requests.get(f'https://ipapi.co/{search}/json/?key=V27xzP081ObqkaS8qJvRDHq8DEFMoULOKsqVhBcZkw0rYwBH0Q').json()
    return render_template('index.html', data=data)


    


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

# CountryName
@app.route('/countryname', methods = ['GET'])
def get_countryName():
    return {'Country Name' : response.get('country_name')}

# Timezone
@app.route('/timezone', methods = ['GET'])
def get_timezone():
    return {'Timezone' : response.get('timezone')}

#Postal/Zip Code
@app.route('/postal', methods = ['GET'])
def get_postal():
        return {'Postal/Zip Code' : response['postal']}

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

#Currency
@app.route('/currency', methods = ['GET'])
def get_currency():
        return {'Currency' : response['currency']}

#Currency Name
@app.route('/currency_name', methods = ['GET'])
def get_CurrencyName():
        return {'Currency Name' : response['currency_name']}

#Languages
@app.route('/languages', methods = ['GET'])
def get_languages():
        return {'Languages' : response['languages']}

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
        "Postal/Zip Code": response.get("postal"),
        "Latitude": response.get("latitude"),
        "Longitude": response.get("longitude"),
        "Timezone": response.get("timezone"),
        "Currency": response.get("currency"),
        "Currency Name": response.get("currency_name"),
        "Languages" : response.get("languages")
    }
    return data
    
if __name__ == "__main__":
    app.run()