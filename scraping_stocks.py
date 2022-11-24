from bs4 import BeautifulSoup
import requests
import time
stock = input("Enter stock ticker: ")
stock = stock.upper()

url = f"https://finance.yahoo.com/quote/{stock}"

result = requests.get(url)
doc = BeautifulSoup(result.text,"html.parser")




match = doc.find('section',id='similar-by-symbol')

table = match.find('table')
tbody = table.find('tbody')
a = tbody.find_all('a')
similar_stocks = []
for i in a:
    similar_stocks.append(i.text)


match = doc.find('div',id="Col2-9-QuoteModule-Proxy")

div = match.find('div')
sec = div.find('section')
div=sec.find('div')
divf = div.find('div')

analyst_rec = divf.text


match = doc.find("div",id="Col2-10-QuoteModule-Proxy")
div = match.find('div')
sec = div.find('section')
div = sec.find('div')
divlo = div.find('div',class_="Ov(a) Fz(xs) Mt(10px) C($tertiaryColor)")
price_low = divlo.find_all('span')[1].text
divlo = div.find('div',class_="Pos(r) Fl(end) Fz(xs) C($tertiaryColor)")
price_high = divlo.find_all('span')[1].text

divlo = div.find('div',class_="Pos(r) Pb(30px) H(1em)")
divpr = divlo.find('div',class_="Pos(a) D(ib) T(35px)")
divh = divpr.find_all('div')[2]
price_current = divh.find_all('span')[1].text

divpr=divlo.find('div',class_="Pos(a) D(ib) T(-1px)")
divh = divpr.find('div')
price_avg = divh.find_all('span')[1].text



print("Similar stocks are : " ,similar_stocks)
print("Analyst Recommendation: " , analyst_rec)
print("Low price : ",price_low)
print("Current Price : " , price_current)
print("Price average" , price_avg)
print("High price: ", price_high)

time.sleep(5)