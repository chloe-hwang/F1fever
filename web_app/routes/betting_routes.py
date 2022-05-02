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

    results = get_betting_results(season_code=season_code, round_code=round_code)
    
    return render_template("betting_results.html", results=results)





    #if results:
    #    flash("Betting Results Generated Successfully!", "success")
    #    return render_template("betting_results.html", results=results)
    #else:
    #    flash("The Grand Prix has not taken place yet! Please try again at a later time!", "danger")
    #    return redirect("/betting/form") 
    
  





    
