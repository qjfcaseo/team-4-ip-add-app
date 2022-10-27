# Getting the ASN
from flask import Flask
from requests import get

app = Flask (__name__)

response = get('https://ipapi.co/json/').json()

@app.route('/asn', methods = ['GET'])
def get_asn():
        return {'ASN' : response['asn']}

if __name__ == "__main__":    
    app.run()


