# Getting the Languages
from flask import Flask
from requests import get

app = Flask (__name__)

response = get('https://ipapi.co/json/').json()

@app.route('/languages', methods = ['GET'])
def get_languages():
        return {'Languages' : response['languages']}

if __name__ == "__main__":    
    app.run()


