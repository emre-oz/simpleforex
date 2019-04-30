import requests

def url_define_latest(base=None, symbols=None):
    
    url = "https://api.exchangeratesapi.io/latest"
    
    if base != "":
        url = url + "?base=" + str(base) 
    else:
        url = url
    
    return url


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
        
    dict["rate"] = cur_list
    dict["currency"] = rate_list
    
    return dict


print(fetch_latest())