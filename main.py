import requests
import re
from bs4 import BeautifulSoup



#------------------------------------------------------------------------------------------------

res1=requests.get("https://www.tgju.org/")
soup1=BeautifulSoup(res1.content,"html.parser")

res2=requests.get("https://arzdigital.com/coins/tether/")
soup2=BeautifulSoup(res2.content,"html.parser")

res3=requests.get("https://ramzarz.news/coins/tether/")
soup3=BeautifulSoup(res3.content,"html.parser")

assert res1.status_code == 200 , "There is sth wrong in res1"
assert res2.status_code == 200 , "There is sth wrong in res2"
assert res3.status_code == 200 , "There is sth wrong in res3"





coin_names=["BTC","ETH","Litecoin","BitcoinCash","USDT","Tron","BNB","XLM","XRP","DogeCoin","Dash","ADA","DOT","SOL","AVAX"]
# coin_names=["BTC","ETH","BNB","XLM","XRP","DogeCoin","ADA","DOT","SOL","AVAX"]
# coin_names=[]
coin_prices=[]





data_coins=soup1.select("td.market-price-irr")

for currency in data_coins:
        names=currency["data-market-p"]
        prices=currency.text.strip()
        # most_coins=re.findall(r"'crypto-(\w*)-irr'",names)
        # two_coins=re.findall(r"'crypto-(\w*-\w*)-irr'",names)
       
        
        # coin_names.append(most_coins)
        # coin_names.append(two_coins)
        coin_prices.append(prices)


first_list=[i.replace(",", "") for i in coin_prices]
toman_coins=[int(x)//10 for x in first_list]
        

usdt_tgju=toman_coins[4]
usdt_coins=[element/usdt_tgju for element in toman_coins]    


usdt_soup2 = soup2.select("form>div>div>div>input")
usdt_arzdigital="".join([element["value"] for element in usdt_soup2])
usdt_arzdigital2="".join(re.findall(r"1\.00\s*(\d*,\d*)",usdt_arzdigital))


usdt_soup3 = soup3.select("div.coin-price-btc")
usdt_ramzarz="".join([element.text.strip() for element in usdt_soup3])
usdt_ramzarz="".join(re.findall(r"(\d*,\d*)",usdt_ramzarz))





final_toman_list=toman_coins.copy()
final_usdt_list=usdt_coins.copy()
final_toman_list.pop(10)
final_toman_list.pop(5)
final_toman_list.pop(4)
final_toman_list.pop(3)
final_toman_list.pop(2)
final_usdt_list.pop(10)
final_usdt_list.pop(5)
final_usdt_list.pop(4)
final_usdt_list.pop(3)
final_usdt_list.pop(2)

# print(toman_coins)
# print(50*"-")
# print(usdt_coins)





def coins_calculated_by_toman():
        zipfile_toman=zip(coin_names,toman_coins)
        for name,price in zipfile_toman:
                print(f"{name}: {price}")


def coins_calculated_by_usdt():
        zipfile_usdt=zip(coin_names,usdt_coins)
        for name,price in zipfile_usdt:
                print(f"{name}: {price}")


def usdt_rate():
        print(f"""
USDT Rate in tgju: {usdt_tgju} 
USDT Rate in arzdigita: {usdt_arzdigital2}
USDT Rate in ramzarz: {usdt_ramzarz}""")

# coins_calculated_by_toman()
# coins_calculated_by_usdt()
# usdt_rate()