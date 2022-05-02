from flask import Blueprint, request, render_template, flash, redirect

from app.results import get_betting_results

betting_routes = Blueprint("betting_routes", __name__)

@betting_routes.route("/betting/form")
def betting_form():
    print("Betting FORM...")
    return render_template("betting_form.html")

@betting_routes.route("/betting/results", methods=["GET", "POST"])
def betting_results():
    print("Betting RESULTS...")

    if request.method == "GET":
        print("URL PARAMS:", dict(request.args))
        request_data = dict(request.args)
    elif request.method == "POST": # the form will send a POST
        print("FORM DATA:", dict(request.form))
        request_data = dict(request.form)

    season_code = request_data.get("season") or "2022"
    round_code = request_data.get("round") or "1"
    winner_user_input_code = request_data.get("winner_user_input") or "Lewis Hamilton"

    results = get_betting_results(season_code=season_code, round_code=round_code)

    given_name = results[0]["Results"][0]["Driver"]["givenName"]
    family_name = results[0]["Results"][0]["Driver"]["familyName"]
    winner_actual = given_name + " " + family_name
    
    print(given_name)
    print(family_name)
    print(winner_actual)

    if winner_actual == winner_user_input_code:
       bet_code = "right"
    else:
       bet_code = "wrong" 

    print(bet_code)

    if results:
        flash("Betting Results Generated Successfully!", "success")
        return render_template("betting_results.html", results=results, winner_user_input_code=winner_user_input_code, bet_code=bet_code)
    else:
        flash("The Grand Prix has not taken place yet! Please try again at a later time!", "danger")
        return redirect("/betting/form")


 
    
  





    
