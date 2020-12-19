from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from lxml import html

'''
url = "https://www.bestbuy.com/site/amd-ryzen-9-5950x-4th-gen-16-core-32-threads-unlocked-desktop-processor-without-cooler/6438941.p?skuId=6438941"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64;     x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding": "gzip, deflate",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

stock = soup.find_all(
    'div', id='fulfillment-add-to-cart-button-b62e556c-ef03-4281-963e-d6b0147a68ce')

print(stock)

if str(stock) == '[]':
    print("In Stock")
else:
    print("Out of Stock")

'''
'''
page = requests.get(
    'https://www.bestbuy.com/site/amd-ryzen-9-5950x-4th-gen-16-core-32-threads-unlocked-desktop-processor-without-cooler/6438941.p?skuId=6438941')
tree = html.fromstring(page.content)
stock = tree.xpath(
    '/html/body/div[3]/main/text()')
print(stock)
'''


browser = webdriver.Chrome()
browser.get("https://www.bestbuy.com/site/amd-ryzen-9-5950x-4th-gen-16-core-32-threads-unlocked-desktop-processor-without-cooler/6438941.p?skuId=6438941")
timestamp = browser.find_element_by_xpath('/html/body/div[3]/main/')
print(timestamp)
