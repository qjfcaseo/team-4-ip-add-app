from flask import Flask 
from requests import get
from flask_restful import Resource

app = Flask (__name__)

response = requests.get('https://ipapi.co/json/').json()

class ipAddress(Resource):
    def get_ip(self):
        myIP = response['ip']
        return myIP

    


# response = get('https://ipapi.co/json/').json()
# @app.route('/ip', methods = ['GET'])
# def get_ip():
#     return {'IP Address': response['ip']}


# if _name_ == "_main_":
#     app.run()


# def get_ip():
#     response = get('https://ipapi.co/json/').json()
#     return response["ip"]
# print(get_ip())