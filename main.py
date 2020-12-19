from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.com/amd-ryzen-5-3600/p/N82E16819113569"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64;     x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding": "gzip, deflate",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

stock = soup.find_all(
    'div', id="availability", class_="a-section a-spacing-base")

print(stock)

if str(stock) == '[]':
    print("In Stock")
else:
    print("Out of Stock")
