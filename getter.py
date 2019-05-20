import requests
from url_define import url_define_latest, url_define_day, url_define_period, url_define_live
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
import time
from werkzeug.contrib.cache import SimpleCache

#Instance of SimpleCache object
cache=SimpleCache()

#/latest route
def fetch_latest(base="EUR"):
    url = url_define_latest(base)
    r=requests.get(url)
    response_dict = r.json()
    sum_data = []
    cur_list = []
    rate_list = []
    dict = {}
    
    for cur, rate in response_dict["rates"].items():
        sum_data.append(cur)
        sum_data.append(rate)

    for i in range(0,len(sum_data),2):
        cur_list.append(sum_data[i])
    for j in range(1,len(sum_data),2):
        rate_list.append(sum_data[j])
        
    dict["currency"] = cur_list
    dict["rate"] = rate_list
    
    return dict

#input: "/daily" route ; output: "/daily_data" route
def fetch_daily(date, symbols, base="EUR"):
    url=url_define_day(date,base,symbols)
    r=requests.get(url)
    response_dict=r.json()
    array=[]
    for currency in response_dict["rates"].items():
        array.append(currency)
    daily_rates=dict(array)

    return daily_rates

#input: "/period" route ; output: "/period_data" route
def fetch_period(start_date,end_date,symbols,base="EUR"):
    url=url_define_period(start_date,end_date,symbols,base)
    r=requests.get(url)
    response_dict=r.json()
    ratelist=[]

    #Data wrangling
    for tradingday in sorted(response_dict["rates"].keys()):
        plot_dict = {"value" : response_dict["rates"][tradingday][symbols], "label" : str(tradingday)}
        ratelist.append(plot_dict)
    

    #Styling and configuration of chart
    my_style = LS("#333366" , base_style = LCS)
    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.show_legend = True
    my_config.title_font_size = 24
    my_config.label_font_size = 14
    my_config.major_label_font_size = 18
    my_config.truncate_label = 15
    my_config.show_y_guides = True
    my_config.width = 1000
    chart=pygal.Line(my_config, style= my_style)

    #Char title specification
    if base == "":
        basetitle = "EUR"
    else:
        basetitle = base
    chart.title = basetitle + "/" + symbols + " exchange rate for the period: " + start_date + "/" + end_date
    chart.add("",ratelist)
    chart_data = chart
    
    return chart_data

#"/index" and "/" route
def fetch_live():
    
    url= url_define_live()
    r= requests.get(url)
    response_dict=r.json()
    pair_list = []
    rate_list=[]
    timestamp_list = []
    live_dict ={}

    for pairs, rates in response_dict["rates"].items():

        pairs = pairs[3:] + "/" +pairs[:3]
        pair_list.append(pairs)

        rate = rates["rate"]
        epoch_time = rates["timestamp"]
        timestamp = time.strftime("%d/%m %H:%M:%S", time.gmtime(epoch_time))
        
        rate_list.append(rate)
        timestamp_list.append(timestamp)
    
    live_dict["pairs"]= pair_list
    live_dict["rates"]= rate_list
    live_dict["timestamps"]= timestamp_list

    return live_dict

#Calls the fetch_live function and caches result for 10 minutes if no result is found in cache
def fetch_cached_live():
    live_dict = cache.get("cached_live_dict")
    if live_dict is None:
        live_dict = fetch_live()
        cache.set("cached_live_dict", live_dict, timeout =10*60)

    return live_dict

#Calls the fetch_latest function and caches result for 60 minutes if no result is found in cache
def fetch_cached_latest():
    dict = cache.get("cached_latest_dict")
    if dict is None:
        dict = fetch_latest()
        cache.set("cached_latest_dict", dict, timeout= 60*60)

    return dict
    
def fetch_latest_crypto():
    url = "https://api.coinlore.com/api/tickers/"
    r=requests.get(url)
    response_dict = r.json()
    volume_data = []
    name_data = []
    price_data = []
    percent_change = []
    crypto_dict = {}
    
    for i in range(0,100):
        a = response_dict["data"][i]["symbol"]
        name_data.append(a)

    for i in range(0,100):
        b = response_dict["data"][i]["price_usd"]
        price_data.append(b)

    for i in range(0,100):
        c = response_dict["data"][i]["volume24"]
        volume_data.append(c)
    
    for i in range(0,100):
        d = response_dict["data"][i]["percent_change_24h"]
        percent_change.append(d)

    crypto_dict["name"] = name_data
    crypto_dict["price"] = price_data
    crypto_dict["percent_change"] = volume_data
    crypto_dict["volume"] = percent_change

    
    return crypto_dict

def fetch_cached_latest_crypto():
    crypto_dict = cache.get("cached_crypto_dict")
    if crypto_dict is None:
        crypto_dict = fetch_latest_crypto()
        cache.set("cached_crypto_dict", crypto_dict, timeout= 60*60)

    return crypto_dict