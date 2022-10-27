# Gets geo location of the computer using API (ipapi.co)
from flask import Flask
import requests

app = Flask(__name__)

def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]

@app.route('/geoloc', methods = ['GET'])
def get_geoloc():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "country": response.get("country_name"),
        "continent_code": response.get("continent_code"),
        "region": response.get("region"),
        "country_capital": response.get("country_capital"),
        "city": response.get("city"),
        "latitude": response.get("latitude"),
        "longitude": response.get("longitude")
    }
    return location_data

if __name__ == "__main__":
    app.run()