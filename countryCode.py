from requests import get


def get_ip():
    response = get('https://ipapi.co/json/').json()
    return response["country_code"]
print(get_ip())