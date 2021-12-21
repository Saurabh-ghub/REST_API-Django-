import requests
URL="http://127.0.0.1:8000/studentmark/2"
 
r=requests.get(url=URL)
data = r.json()
print(data)