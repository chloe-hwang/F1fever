import requests

url = "http://ergast.com/api/f1/current/last/results"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)