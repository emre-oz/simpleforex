import requests

def url_define_live(from_currency,to_currency):
    url= "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&"
    api_key = "PXHH820C97TBS0JI"
    
    url="https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=" \
        + from_currency + "&to_currency=" + to_currency + "&apikey=" + api_key
    
    return url

def fetch_live(from_currency,to_currency):
    url= url_define_live(from_currency,to_currency)
    r= requests.get(url)
    response_dict=r.json()
    rate= response_dict["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
    refresh= response_dict["Realtime Currency Exchange Rate"]["6. Last Refreshed"]
    timezone= response_dict["Realtime Currency Exchange Rate"]["7. Time Zone"]
    return rate, refresh, timezone


print(fetch_live("USD","SEK"))


