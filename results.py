import requests 
import json
from pprint import pprint

url = "http://www.ergast.com/api/f1/current/last/results.json"
response = requests.get(url)
result = json.loads(response.text)
data = result['MRData']
results = data["RaceTable"]["Races"]

print("Race Results For The", results[0]["raceName"], results[0]["season"],":")

race_result = results[0]["Results"]


for index, d in enumerate(race_result, start=1):
    print(index, "-", d["Driver"]["givenName"], d["Driver"]["familyName"])