import requests
from url_define import url_define_latest, url_define_day, url_define_period, url_list_define_live    
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


def fetch_latest(base="EUR"):
    url = url_define_latest(base)
    r=requests.get(url)
    response_dict = r.json()
    array=[]
    
    for currency in response_dict["rates"].items():
        array.append(currency)
    news=dict(array)

    return news

def fetch_daily(date, symbols, base="EUR"):
    url=url_define_day(date,base,symbols)
    r=requests.get(url)
    response_dict=r.json()
    array=[]
    for currency in response_dict["rates"].items():
        array.append(currency)
    daily_rates=dict(array)

    return daily_rates

def fetch_period(start_date,end_date,symbols,base="EUR"):
    url=url_define_period(start_date,end_date,symbols,base)
    r=requests.get(url)
    response_dict=r.json()
    ratelist=[]

    for tradingday in sorted(response_dict["rates"].keys()):
        plot_dict = {"value" : response_dict["rates"][tradingday][symbols], "label" : str(tradingday)}
        ratelist.append(plot_dict)
    
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

    if base == "":
        basetitle = "EUR"
    else:
        basetitle = base

    chart.title = basetitle + "/" + symbols + " exchange rate for the period: " + start_date + "/" + end_date

    chart.add("",ratelist)

    chart_data = chart
    
    return chart_data

def fetch_url_list():
    url_list = url_list_define_live()
    sum_data = []
    
    for url in url_list:
        r = requests.get(url)
        response_dict=r.json()
        
        from_cur = response_dict["Realtime Currency Exchange Rate"]["1. From_Currency Code"]
        to_cur = response_dict["Realtime Currency Exchange Rate"]["3. To_Currency Code"]
        divide = str(from_cur + "/" + to_cur)
        sum_data.append(divide)
        rate= response_dict["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
        sum_data.append(rate)
        refresh= response_dict["Realtime Currency Exchange Rate"]["6. Last Refreshed"]
        sum_data.append(refresh)
        timezone= response_dict["Realtime Currency Exchange Rate"]["7. Time Zone"]
        sum_data.append(timezone)

    list1=[sum_data[i] for i in range(0,4)]
    list2=[sum_data[i] for i in range(4,8)]
    list3=[sum_data[i] for i in range(8,12)]
    list4=[sum_data[i] for i in range(12,16)]
    list5=[sum_data[i] for i in range(16,20)]

    return list1,list2,list3,list4,list5

        





"""
def fetch_live(from_currency,to_currency):
    url= url_define_live(from_currency,to_currency)
    r= requests.get(url)
    response_dict=r.json()
    rate= response_dict["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
    refresh= response_dict["Realtime Currency Exchange Rate"]["6. Last Refreshed"]
    timezone= response_dict["Realtime Currency Exchange Rate"]["7. Time Zone"]
    return rate, refresh, timezone
"""

