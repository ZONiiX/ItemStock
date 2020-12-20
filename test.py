from bs4 import BeautifulSoup
import requests
import hashlib
from lxml.html import fromstring

url = "https://www.amazon.com/Female-Connector-Antenna-Pigtail-Extension/dp/B071HJN1H9/?_encoding=UTF8&pd_rd_w=BcBgr&pf_rd_p=c638e3d4-046b-4753-9e53-3752c2d7f6a7&pf_rd_r=QZET14T806NBAJZ6D9E8&pd_rd_r=d7924794-c544-45b5-88d6-bfa69badfa6a&pd_rd_wg=vjKYW&ref_=pd_gw_hl_comp_mis_psims"
headers = {
    'authority': 'www.amazon.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}


page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

stock = soup.find(id='priceblock_ourprice')
isStock = 0

print(stock)


if stock == None:
    isStock = 0
    print("Item is not in stock")
else:
    isStock = 1
    print("Item is in stock")


# 4f787970885f6093097e85899aa22a1d8f31ad23a7739cf47afe84a76790d22
