
# loc = get('https://ipapi.co/json/')
# print (loc.json())
# from flask import Flask
from requests import get


def get_ip():
    response = get('https://ipapi.co/json/').json()
    return response["ip"]
print(get_ip())
