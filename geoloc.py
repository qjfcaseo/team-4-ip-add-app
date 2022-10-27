# Gets geo location of the computer (Angel)
from requests import get

loc = get('https://ipapi.co/json/')
print (loc.json())