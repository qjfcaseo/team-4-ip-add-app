# Getting the Zip Code
from flask import Flask
from requests import get

app = Flask (__name__)

response = get('https://ipapi.co/json/').json()

@app.route('/postal', methods = ['GET'])
def get_postal():
        return {'Postal/Zip Code' : response['postal']}

if __name__ == "__main__":    
    app.run()


