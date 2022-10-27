import requests

BASE = 'http://127.0.0.1:5000/'

response = request.get(BASE + 'product/2')
print(response.json())


