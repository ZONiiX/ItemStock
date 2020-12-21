from requests_html import HTMLSession
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

amazon_products = open('Lists/amazonlist.txt').readlines()


def getAmazonStock(url, header):
    session = HTMLSession()
    result = session.get(url, headers=header)
    result.html.render(sleep=1)

    try:
        product = {
            'Amazon US': result.html.xpath('//*[@id="productTitle"]', first=True).text,
            'Price': result.html.xpath('//*[@id="priceblock_ourprice"]', first=True).text,
            'Stock': result.html.xpath('//*[@id="availability_feature_div"]', first=True).text
        }
    except:
        product = {
            'Amazon US': result.html.xpath('//*[@id="productTitle"]', first=True).text,
            'Price': 'Price unavailable',
            'Stock': '*Out of stock*'
        }

    if product['Stock'] == "*Out of stock*":
        None
    else:
        product['Stock'] = '*In stock*'

    StylizedPrice = ''
    StylizedProduct = ''

    if product['Price'] == 'Price unavailable' and product['Stock'] == '*Out of stock*':
        StylizedPrice = Fore.RED + Style.BRIGHT + product["Price"]
        StylizedProduct = Fore.RED + Style.BRIGHT + product["Stock"]
    elif product['Price'] != 'Price unavailable' and product['Stock'] != "*Out of stock*":
        StylizedPrice = Fore.GREEN + Style.BRIGHT + product["Price"]
        StylizedProduct = Fore.GREEN + Style.BRIGHT + product["Stock"]
    elif product['Price'] == 'Price unavailable' and product['Stock'] != "*Out of stock*":
        StylizedPrice = Fore.RED + Style.BRIGHT + product["Price"]
        StylizedProduct = Fore.GREEN + Style.BRIGHT + product["Stock"]
    elif product['Price'] != 'Price unavailable' and product['Stock'] == '*Out of stock*':
        StylizedPrice = Fore.GREEN + Style.BRIGHT + product["Price"]
        StylizedProduct = Fore.RED + Style.BRIGHT + product["Stock"]

    print(Fore.BLUE + "[Amazon US]" + "  " +
          "\033[39m" + product["Amazon US"] + "  " + StylizedPrice + "  " + "\033[39m" + StylizedProduct)

    return product


def loopAmazonStock():
    for url in amazon_products:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
        getAmazonStock(url, headers)
