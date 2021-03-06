from app import app
from flask import render_template, request, redirect, url_for
from app.forms import DailyForm, PeriodForm
from flask_wtf import FlaskForm
from getter import fetch_cached_latest, fetch_daily, fetch_period, fetch_cached_live, fetch_cached_latest_crypto


@app.route("/")
@app.route("/index")
def index():
    live_dict = fetch_cached_live()
    
    return render_template("index.html",title="Home", live_dict=live_dict)

@app.route("/latest", methods=["GET","POST"])
def latest():
    dict = fetch_cached_latest()
    return render_template("latest.html", dict=dict, title="Latest Exchange Rates")

#HTML posts user input to "/daily_data"
@app.route("/daily",methods=["GET","POST"])
def daily():
    daily_form=DailyForm()
    return render_template("daily.html", title="Daily Exchange Rates", form= daily_form)

#INPUT: "GET" request to "/daily" route
@app.route("/daily_data", methods=["GET","POST"])
def daily_data():
    date= request.form.get("day")
    base= request.form.get("base")
    symbols= request.form.get("symbols")
    daily_rates= fetch_daily(date, symbols, base)
    
    return render_template("daily_data.html",title="Daily Exchange Rates",daily_rates=daily_rates,date=date)

#HTML posts user input to "/period_data"
@app.route("/period",methods=["GET","POST"])
def period():
    period_form=PeriodForm()
    return render_template("period.html", title="Exchange Rates for Period",form=period_form)

#INPUT: "GET" request to "/period" route
@app.route("/period_data",methods=["GET","POST"])
def period_data():
    start_day= request.form.get("start_day")
    end_day= request.form.get("end_day")
    base= request.form.get("base")
    symbols= request.form.get("symbols")
    chart = fetch_period(start_day,end_day,symbols,base)
    return render_template("period_data.html", chart= chart, title= "Currency Information")

@app.route("/crypto",methods=["GET","POST"])
def crypto():
    crypto_dict = fetch_cached_latest_crypto()
    return render_template("crypto.html", crypto_dict = crypto_dict, title="Cryptocurrency Information")

@app.route("/about", methods=["GET","POST"])
def about():
    return render_template("about.html", title= "About")