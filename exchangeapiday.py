
import requests
from url_define import url_define_day

date = input("Date(YYYY-MM-DD): ")
symbols = input("Symbols: ") 
base = input("Base: ")

url = url_define_day(date, symbols, base)

r=requests.get(url)

response_dict = r.json()

print("Exchange rate information for the date: " + response_dict["date"] )

for currency in response_dict["rates"].items():
    print("\n" , currency)