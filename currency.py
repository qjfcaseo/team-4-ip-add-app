# Getting the Currency
from flask import Flask
from requests import get

app = Flask (__name__)

response = get('https://ipapi.co/json/').json()

@app.route('/currency', methods = ['GET'])
def get_currency():
        return {'Currency' : response['currency']}

if __name__ == "__main__":    
    app.run()


