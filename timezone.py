# Getting the Timezone
from flask import Flask
from requests import get

app = Flask (__name__)

response = get('https://ipapi.co/json/').json()

@app.route('/timezone', methods = ['GET'])
def get_languages():
        return {'Timezone' : response['timezone']}

if __name__ == "__main__":    
    app.run()