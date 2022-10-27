
from flask import Flask
from requests import get

app = Flask(__name__)

response = get('https://ipapi.co/json/').json()

@app.route('/isp', methods = ['GET'])
def get_ip():
    return {'ISP': response['org']}

    


if __name__ == "__main__":
    app.run()