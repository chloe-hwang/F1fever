import requests 
import json
from pprint import pprint

def get_betting_results(season_code, round_code):

    season_CODE = season_code
    round_CODE = round_code

    url = f"http://www.ergast.com/api/f1/{season_CODE}/{round_CODE}/results.json"
    response = requests.get(url)
    result = json.loads(response.text)
    data = result['MRData']
    results = data["RaceTable"]["Races"]

    return results

