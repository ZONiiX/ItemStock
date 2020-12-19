from bs4 import BeautifulSoup
import requests

url = "https://www.amazon.com/AMD-Ryzen-5600X-12-Thread-Processor/dp/B08166SLDF?ref_=ast_sto_dp"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64;     x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding": "gzip, deflate",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

stock = str(soup.find_all(
    'div', id="availability", class_="a-section a-spacing-base"))

isStock = 0

print(stock)

if stock == str("""[<div class="a-section a-spacing-base" id="availability">
<span class="a-size-medium a-color-price">


Currently unavailable.









</span>
<br/>We don't know when or if this item will be back in stock.





</div>]"""):
    isStock = 0
    print("Item is not in stock")
else:
    isStock = 1
    print("Item is in stock")
