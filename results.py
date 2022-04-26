import requests 
import json
from pprint import pprint

url = "http://www.ergast.com/api/f1/current/last/results.json"
response = requests.get(url)
result = json.loads(response.text)
data = result['MRData']
results = data["RaceTable"]["Races"]

print("Race Results For The", results[0]["raceName"],":")


race_result = results[0]["Results"]


for d in race_result:
    print(d["Driver"]["givenName"], d["Driver"]["familyName"])