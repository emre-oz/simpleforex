
import requests
from url_define import url_define_latest

symbols = input("Symbols: ") 
base = input("Base: ")


url = url_define_latest(symbols,base)

r=requests.get(url)

response_dict = r.json()

print("Exchange rate information for the date: " + response_dict["date"] )
print(response_dict)

"""
for currency in response_dict["rates"].items():
    print("\n" , currency)

"""