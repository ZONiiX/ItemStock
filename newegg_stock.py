from requests_html import HTMLSession
import colorama
from colorama import Fore, Back, Style

newegg_products = open('Lists/newegglist.txt').readlines()


def getNeweggStock(url):
    session = HTMLSession()
    result = session.get(url)
    result.html.render(sleep=1)

    product = {
        'Newegg US': result.html.xpath('//*[@id="app"]/div[2]/div[1]/div/div/div[2]/div[1]/div[5]/h1', first=True).text,
        'Price': result.html.xpath('//*[@id="app"]/div[2]/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/ul/li[3]', first=True).text,
        'Stock': result.html.xpath('//*[@id="ProductBuy"]', first=True).text
    }
    if product['Stock'] == 'Sold Out':
        product['Stock'] = '*Out of stock*'
    else:
        product['Stock'] = '*In Stock*'

    StylizedPrice = ''
    StylizedProduct = ''

    if product['Price'] == 'Unavailable' and product['Stock'] == '*Out of stock*':
        StylizedPrice = Fore.RED + Style.BRIGHT + product["Price"]
        StylizedProduct = Fore.RED + Style.BRIGHT + product["Stock"]
    elif product['Price'] != 'Unavailable' and product['Stock'] != "*Out of stock*":
        StylizedPrice = Fore.GREEN + Style.BRIGHT + product["Price"]
        StylizedProduct = Fore.GREEN + Style.BRIGHT + product["Stock"]
    elif product['Price'] == 'Unavailable' and product['Stock'] != "*Out of stock*":
        StylizedPrice = Fore.RED + Style.BRIGHT + product["Price"]
        StylizedProduct = Fore.GREEN + Style.BRIGHT + product["Stock"]
    elif product['Price'] != 'Unavailable' and product['Stock'] == '*Out of stock*':
        StylizedPrice = Fore.GREEN + Style.BRIGHT + product["Price"]
        StylizedProduct = Fore.RED + Style.BRIGHT + product["Stock"]

    print(Fore.BLUE + "[Newegg US]" + "  " +
          "\033[39m" + product["Newegg US"] + "  " + StylizedPrice + "  " + "\033[39m" + StylizedProduct)

    return product


def loopNeweggStock():
    for url in newegg_products:
        getNeweggStock(url)
