from bs4 import BeautifulSoup
from datetime import datetime
import requests


newegg_products = {
    "NeweggUS Ryzen 5 5600x": "https://www.newegg.com/amd-ryzen-5-5600x/p/N82E16819113666?Description=ryzen&cm_re=ryzen-_-19-113-666-_-Product",
    "NeweggUS Ryzen 7 5800x": "https://www.newegg.com/amd-ryzen-7-5800x/p/N82E16819113665?Description=ryzen%205700&cm_re=ryzen_5700-_-19-113-665-_-Product",
    "NeweggUS Ryzen 9 5900x": "https://www.newegg.com/amd-ryzen-9-5900x/p/N82E16819113664?Description=ryzen%205700&cm_re=ryzen_5700-_-19-113-664-_-Product",
    "NeweggUS Ryzen 9 5950x": "https://www.newegg.com/amd-ryzen-9-5900x/p/N82E16819113664?Description=ryzen%205700&cm_re=ryzen_5700-_-19-113-664-_-Product"
}

amazon_products = {
    "AmazonUS Ryzen 5 5600x": "https://www.amazon.com/AMD-Ryzen-5600X-12-Thread-Processor/dp/B08166SLDF?ref_=ast_sto_dp",
    "AmazonUS Ryzen 7 5800x": "https://www.amazon.com/AMD-Ryzen-5800X-16-Thread-Processor/dp/B0815XFSGK?ref_=ast_sto_dp",
    "AmazonUS Ryzen 9 5900x": "https://www.amazon.com/Ryzen-5900X-12-Core-Desktop-Processor/dp/B08NXYLBN5/ref=sr_1_3?dchild=1&keywords=ryzen+9+5900x&qid=1608348416&s=electronics&sr=1-3",
    "AmazonUS Ryzen 9 5950x": "https://www.amazon.com/AMD-Ryzen-5950X-32-Thread-Processor/dp/B0815Y8J9N?ref_=ast_sto_dp"
}

bestbuy_products = {
    "BestBuyUS Ryzen 5 5600x": "https://www.bestbuy.com/site/amd-ryzen-5-5600x-4th-gen-6-core-12-threads-unlocked-desktop-processor-with-wraith-stealth-cooler/6438943.p?skuId=6438943"
    "BestBuyUS Ryzen 7 5800x": "https://www.bestbuy.com/site/amd-ryzen-7-5800x-4th-gen-8-core-16-threads-unlocked-desktop-processor-without-cooler/6439000.p?skuId=6439000"
    "BestBuyUS Ryzen 9 5900x": "https://www.bestbuy.com/site/amd-ryzen-9-5900x-4th-gen-12-core-24-threads-unlocked-desktop-processor-without-cooler/6438942.p?skuId=6438942"
    "BestBuyUS Ryzen 9 5950x": "https://www.bestbuy.com/site/amd-ryzen-9-5950x-4th-gen-16-core-32-threads-unlocked-desktop-processor-without-cooler/6438941.p?skuId=6438941"
}


def findNeweggStock(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    stock = soup.find_all('div', class_="product-inventory")
   # print(soup.find_all('div', class_="product-inventory"))

    if str(stock) == '[<div class="product-inventory"><strong><i class="fas fa-exclamation-triangle"></i> OUT OF STOCK.</strong></div>]':
        return(0)
    else:
        return(1)


def findAmazonStock(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64;     x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding": "gzip, deflate",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    stock = soup.find_all(
        'div', id="availability", class_="a-section a-spacing-base")

    if str(stock) != '[]':
        return(0)
    else:
        return(1)


repeat = True
while repeat == True:
    for key in newegg_products:
        if findNeweggStock(newegg_products[key]) == 0:
            now = datetime.now()
            print(key, "Out of Stock", "  UPDATED:",
                  now.strftime("%m/%d/%Y %H:%M:%S"))
        else:
            now = datetime.now()
            print(key, "In Stock", "  UPDATED:",
                  now.strftime("%m/%d/%Y %H:%M:%S"))

    for key in amazon_products:
        if findAmazonStock(amazon_products[key]) == 0:
            now = datetime.now()
            print(key, "Out of Stock", "  UPDATED:",
                  now.strftime("%m/%d/%Y %H:%M:%S"))
        else:
            now = datetime.now()
            print(key, "In stock", "  UPDATED:",
                  now.strftime("%m/%d/%Y %H:%M:%S"))
    repeat = True
