from app import app
from flask import render_template, request, redirect, url_for
from app.forms import DailyForm, PeriodForm
from flask_wtf import FlaskForm
from getter import fetch_cached_latest, fetch_daily, fetch_period, fetch_cached_live


@app.route("/")
@app.route("/index")
def index():
    live_dict = fetch_cached_live()
    
    return render_template("index.html",title="Home", live_dict=live_dict)

@app.route("/latest", methods=["GET","POST"])
def latest():
    dict = fetch_cached_latest()
    return render_template("latest.html", dict=dict, title="Latest Exchange Rates")


@app.route("/daily",methods=["GET","POST"])
def daily():
    daily_form=DailyForm()
    return render_template("daily.html", title="Daily Exchange Rates", form= daily_form)

@app.route("/daily_data", methods=["GET","POST"])
def daily_data():
    date= request.form.get("day")
    base= request.form.get("base")
    symbols= request.form.get("symbols")
    daily_rates= fetch_daily(date, symbols, base)
    
    return render_template("daily_data.html",title="Daily Exchange Rates",daily_rates=daily_rates,date=date)

@app.route("/period",methods=["GET","POST"])
def period():
    period_form=PeriodForm()
    return render_template("period.html", title="Exchange Rates for Period",form=period_form)


@app.route("/period_data",methods=["GET","POST"])
def period_data():
    start_day= request.form.get("start_day")
    end_day= request.form.get("end_day")
    base= request.form.get("base")
    symbols= request.form.get("symbols")
    chart_data = fetch_period(start_day,end_day,symbols,base)
    return chart_data.render_response()