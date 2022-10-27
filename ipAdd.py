

from flask import Flask
from requests import get

app = Flask(__name__)

response = get('https://ipapi.co/json/').json()

@app.route('/ip', methods = ['GET'])
def get_ip():
    return {'IP Address': response['ip']}

    


if __name__ == "__main__":
    app.run()

# =================================================
# def get_ip():
#     response = get('https://ipapi.co/json/').json()
#     return response["ip"]
# print(get_ip())
