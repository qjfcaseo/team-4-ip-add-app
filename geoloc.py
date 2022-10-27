# Gets geo location of the computer using API (ipapi.co)
from flask import Flask
from flask import response, request
from flask_restful import Resource

class GeoLocation(Resource):
    def get_ip():
        response = requests.get('https://api64.ipify.org?format=json').json()
        return response["ip"]

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

#print(get_geoloc())