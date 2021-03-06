from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField,StringField

#User input form for "/daily"
class DailyForm(FlaskForm):
    base = SelectField("Base Currency:", choices=[("EUR","EUR"),("USD","USD"),("PHP","PHP"),("CHF","CHF"),("ZAR","ZAR"),("AUD","AUD"),("JPY","JPY"),\
        ("TRY","TRY"),("HKD","HKD"),("MYR","MYR"),("THB","THB"),("HRK","HRK"),("NOK","NOK"),("IDR","IDR"),("DKK","DKK"),("CZK","CZK"),\
        ("HUF","HUF"),("GBP","GBP"),("MXN","MXN"),("KRW","KRW"),("ISK","ISK"),("SGD","SGD"),("BRL","BRL"),("PLN","PLN"),("INR","INR"),\
        ("RON","RON"),("CNY","CNY"),("SEK","SEK")])
    symbols = SelectField("Symbols:", choices=[("EUR","EUR"),("USD","USD"),("PHP","PHP"),("CHF","CHF"),("ZAR","ZAR"),("AUD","AUD"),("JPY","JPY"),\
        ("TRY","TRY"),("HKD","HKD"),("MYR","MYR"),("THB","THB"),("HRK","HRK"),("NOK","NOK"),("IDR","IDR"),("DKK","DKK"),("CZK","CZK"),\
        ("HUF","HUF"),("GBP","GBP"),("MXN","MXN"),("KRW","KRW"),("ISK","ISK"),("SGD","SGD"),("BRL","BRL"),("PLN","PLN"),("INR","INR"),\
        ("RON","RON"),("CNY","CNY"),("SEK","SEK")])
    day = StringField("YYYY-MM-DD")
    submit=SubmitField("Get Data")

#User input form for "/period"
class PeriodForm(FlaskForm):
    start_day = StringField("Start date(YYYY-MM-DD)")
    end_day = StringField("End date(YYYY-MM-DD)")
    base = SelectField("Base Currency:", choices=[("EUR","EUR"),("USD","USD"),("PHP","PHP"),("CHF","CHF"),("ZAR","ZAR"),("AUD","AUD"),("JPY","JPY"),\
        ("TRY","TRY"),("HKD","HKD"),("MYR","MYR"),("THB","THB"),("HRK","HRK"),("NOK","NOK"),("IDR","IDR"),("DKK","DKK"),("CZK","CZK"),\
        ("HUF","HUF"),("GBP","GBP"),("MXN","MXN"),("KRW","KRW"),("ISK","ISK"),("SGD","SGD"),("BRL","BRL"),("PLN","PLN"),("INR","INR"),\
        ("RON","RON"),("CNY","CNY"),("SEK","SEK")])
    symbols = SelectField("Symbols:", choices=[("EUR","EUR"),("USD","USD"),("PHP","PHP"),("CHF","CHF"),("ZAR","ZAR"),("AUD","AUD"),("JPY","JPY"),\
        ("TRY","TRY"),("HKD","HKD"),("MYR","MYR"),("THB","THB"),("HRK","HRK"),("NOK","NOK"),("IDR","IDR"),("DKK","DKK"),("CZK","CZK"),\
        ("HUF","HUF"),("GBP","GBP"),("MXN","MXN"),("KRW","KRW"),("ISK","ISK"),("SGD","SGD"),("BRL","BRL"),("PLN","PLN"),("INR","INR"),\
        ("RON","RON"),("CNY","CNY"),("SEK","SEK")])
    submit=SubmitField("Get Data")

