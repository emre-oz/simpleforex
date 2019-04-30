import requests
from url_define import url_define_latest, url_define_day, url_define_period, url_define_live
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
import time

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

def fetch_live():
    
    url= url_define_live()
    r= requests.get(url)
    response_dict=r.json()
    sum_data =[]

    for pairs, rates in response_dict["rates"].items():

        pairs = pairs[3:] + "/" +pairs[:3]
        sum_data.append(pairs)

        rate = rates["rate"]
        epoch_time = rates["timestamp"]
        timestamp = time.strftime("%d/%m %H:%M:%S", time.gmtime(epoch_time))
        
        sum_data.append(rate)
        sum_data.append(timestamp)
        

    l1=sum_data[0:3]
    l2=sum_data[3:6]
    l3=sum_data[6:9]
    l4=sum_data[9:12]
    l5=sum_data[12:15]
    l6=sum_data[15:18]
    l7=sum_data[18:21]
    l8=sum_data[21:24]

    return l1,l2,l3,l4,l5,l6,l7,l8




