
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

def url_define_period(start_date,end_date,symbols=None,base=None):
    url = "https://api.exchangeratesapi.io/"
    

    url = url + "history?start_at=" + start_date + "&end_at=" + end_date
    
    if symbols != "":
        if base!= "":
            url = url + "&symbols=" + symbols + "&base=" + base 
        else:
            url = url + "&symbols=" + symbols

    else:
        if base != "":
            url = url + "&base=" + base 
        else:
            url = url
    
    return url

def fetch_period(start_date,end_date,symbols,base="EUR"):
    url=url_define_period(start_date,end_date,symbols,base)
    r=requests.get(url)
    response_dict=r.json()
    ratelist=[]
    mva_list_global = []
    upperband_list=[]
    lowerband_list=[]
    bandlist=[]

    #Data wrangling
    for tradingday in sorted(response_dict["rates"].keys()):
        plot_dict = {"value" : response_dict["rates"][tradingday][symbols], "label" : str(tradingday)}
        ratelist.append(plot_dict)
        bandlist.append(response_dict["rates"][tradingday][symbols])

    for i in range(19,len(bandlist)):
            
            array=[]
            mva_list=[]
            
            for data in bandlist[slice(i-19,i)]:
                array.append(data)
            
            mva= sum(array) / len(array)
            mva_list_global.append(mva)
            
            for rate in array:
                sqrd_deviation = round(pow(abs(rate-mva), 2), 3)
                mva_list.append(sqrd_deviation)
                sumva = sum(mva_list)
            
            upperband = mva + (2*sumva)
            lowerband = mva - (2*sumva)
            upperband_list.append(upperband)
            lowerband_list.append(lowerband)
            


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


    return print(mva_list_global, upperband_list, lowerband_list)

fetch_period("2018-01-01","2018-03-01","USD")
