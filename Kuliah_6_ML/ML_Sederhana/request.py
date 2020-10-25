import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(
    url, json={'Suhu': 29, 'Salinitas': 32, 'DO': 6.1, 'pH': 7.1})

print(r.json())
