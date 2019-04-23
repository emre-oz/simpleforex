from app import app
from flask import render_template, request
from app.forms import DailyForm, PeriodForm
from flask_wtf import FlaskForm
from getter import fetch_latest,fetch_daily, fetch_period, fetch_url_list

@app.route("/")
@app.route("/index")
def index():
    l1, l2, l3, l4, l5 = fetch_url_list()
    
    return render_template("index.html",title="Home", l1=l1, l2=l2, l3=l3, l4=l4, l5=l5)

@app.route("/latest", methods=["GET","POST"])
def latest():
    news = fetch_latest()
    return render_template("latest.html", news=news, title="Latest Exchange Rates")


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
    
    