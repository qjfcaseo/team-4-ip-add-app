# Getting the ASN
import requests

def get_asn():
    response = requests.get('https://ipapi.co/json/').json()
    return response["asn"]
print (get_asn())


