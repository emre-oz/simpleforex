import random

def url_define_latest(base=None, symbols=None):
    
    url = "https://api.exchangeratesapi.io/latest"
    
    if base != "":
        url = url + "?base=" + str(base) 
    else:
        url = url
    
    return url

def url_define_day(date,base,symbols):
    url = "https://api.exchangeratesapi.io/"
    
    url= url+date
    
    if symbols != "":
        if base!= "":
            url = url + "?symbols=" + symbols + "&base=" + base 
        else:
            url = url + "?symbols=" + symbols

    else:
        if base != "":
            url = url + "?base=" + base 
        else:
            url = url
    
    return url
 
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

def url_list_define_live():
    
    api_key_list= ["PXHH820C97TBS0JI", "F78VTE0TSDMC6MDI", "PDQ22IFJZIFMT8BD", "TRSFDAEBQ7ILZRO1", "9BLO3HP31NMWCZR1"]
    api_key = random.choice(api_key_list)

    fromlist = ["EUR","GBP","USD","USD","EUR"]
    tolist = ["USD","USD","CAD","TRY","TRY"]
    url_list=[]
    for j in range(len(tolist)):
        url_list.append("https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=" \
            + fromlist[j] + "&to_currency=" + tolist[j] + "&apikey=" + api_key)

    return url_list

def url_define_live(from_currency,to_currency):
    url= "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&"
    api_key = "PXHH820C97TBS0JI"
    
    url="https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=" \
        + from_currency + "&to_currency=" + to_currency + "&apikey=" + api_key
    
    return url