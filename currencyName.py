# Getting the Currency Name
from flask import Flask
from requests import get

app = Flask (__name__)

response = get('https://ipapi.co/json/').json()

@app.route('/currency_name', methods = ['GET'])
def get_currencyName():
        return {'Currency Name' : response['currency_name']}

if __name__ == "__main__":    
    app.run()


