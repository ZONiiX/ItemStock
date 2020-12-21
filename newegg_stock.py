from requests_html import HTMLSession
import colorama
from colorama import Fore, Back, Style

newegg_products = ['https://www.newegg.com/amd-ryzen-5-5600x/p/N82E16819113666?Description=ryzen&cm_re=ryzen-_-19-113-666-_-Product', 'https://www.newegg.com/amd-ryzen-7-5800x/p/N82E16819113665?Description=ryzen%205700&cm_re=ryzen_5700-_-19-113-665-_-Product',
                   'https://www.newegg.com/amd-ryzen-9-5900x/p/N82E16819113664?Description=ryzen%205700&cm_re=ryzen_5700-_-19-113-664-_-Product', 'https://www.newegg.com/amd-ryzen-9-5900x/p/N82E16819113664?Description=ryzen%205700&cm_re=ryzen_5700-_-19-113-664-_-Product', 'https://www.newegg.com/amd-ryzen-9-5950x/p/N82E16819113663?Description=Ryzen%209%205950X&cm_re=Ryzen_9%205950X-_-19-113-663-_-Product']


def getNeweggStock(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)

    product = {
        'Newegg US': r.html.xpath('//*[@id="app"]/div[2]/div[1]/div/div/div[2]/div[1]/div[5]/h1', first=True).text,
        'Price': r.html.xpath('//*[@id="app"]/div[2]/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/ul/li[3]', first=True).text,
        'Stock': r.html.xpath('//*[@id="ProductBuy"]', first=True).text
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
