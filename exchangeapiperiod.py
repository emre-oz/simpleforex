


import requests 
import pygal
from url_define import url_define_period

from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

start_date = input("\nStart date for the period(YYYY-MM-DD): ")
end_date=input("\nEnd date for the period(YYYY-MM-DD): ")

#Base choice
base = input("\nRates are quoted against the Euro by default. If you'd like to quote against a different currency, please enter the currency you'd like to quote the rates against(Press Enter if you'd like to leave EUR): ")

#Symbol choice
symbols = input("\nWhat currency would you like to get the rates for?(e.g.= EUR,USD,INR) \nPress Enter if you'd like to get rates against all available currencies: ") 

url = url_define_period(start_date,end_date,symbols,base)
r=requests.get(url)



response_dict = r.json()

print("Diagnostics >>")
print("\nStatus code: " , r.status_code)
print(response_dict.keys())
print("Start at: ", response_dict["start_at"])
print("End at: " , response_dict["end_at"])
print("Base: " , response_dict["base"])
print("Currency: ", symbols)


ratelist = []
datelist = []

for tradingday in sorted(response_dict["rates"].keys()):
    plot_dict = {"value" : response_dict["rates"][tradingday][symbols],
                 "label" : str(tradingday)
                 }
    ratelist.append(plot_dict)
    datelist.append(tradingday)


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
chart.render_to_file("api_exchange_final.svg")

print("Data points: ", len(ratelist))

# print(response_dict["rates"].values())