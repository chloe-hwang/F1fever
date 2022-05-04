#this is the formula_test file 


import os
import pytest

from app.results import get_betting_results 

CI_ENV = os.getenv("CI") == "true"

@pytest.mark.skipif(CI_ENV==True, reason="to avoid issuing HTTP requests on the CI server")
def test_get_betting_results():
    # with valid input, returns the winner and whether or not the bet is correct:
    results = get_betting_results(season_code="2022", round_code="1")
    assert results[0]["raceName"] == "Bahrain Grand Prix"
    assert results[0]["season"] == "2022"

    assert results[0]["Results"][0]["position"] == "1"
    assert results[0]["Results"][0]["Driver"]["givenName"] == "Charles"
    assert results[0]["Results"][0]["Driver"]["familyName"] == "Leclerc"
