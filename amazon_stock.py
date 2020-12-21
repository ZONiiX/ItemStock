from requests_html import HTMLSession
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

amazon_products = ['https://www.amazon.com/AMD-Ryzen-5600X-12-Thread-Processor/dp/B08166SLDF?ref_=ast_sto_dp', 'https://www.amazon.com/AMD-Ryzen-5800X-16-Thread-Processor/dp/B0815XFSGK?ref_=ast_sto_dp',
                   'https://www.amazon.com/Ryzen-5900X-12-Core-Desktop-Processor/dp/B08NXYLBN5/ref=sr_1_3?dchild=1&keywords=ryzen+9+5900x&qid=1608348416&s=electronics&sr=1-3', 'https://www.amazon.com/AMD-Ryzen-5950X-32-Thread-Processor/dp/B0815Y8J9N?ref_=ast_sto_dp']

#amazon_products = ['https://www.amazon.com/AMD-Ryzen-3600-12-Thread-Processor/dp/B07STGGQ18/ref=pd_di_sccai_5?pd_rd_w=aSJmR&pf_rd_p=c9443270-b914-4430-a90b-72e3e7e784e0&pf_rd_r=TSZX18GNQ772059XTBGV&pd_rd_r=18eb92e9-2a10-4fda-b68d-f28693f70a62&pd_rd_wg=62Cxv&pd_rd_i=B07STGGQ18&psc=1']


def getAmazonStock(url, header):
    s = HTMLSession()
    r = s.get(url, headers=header)
    r.html.render(sleep=1)

    try:
        product = {
            'Amazon US': r.html.xpath('//*[@id="productTitle"]', first=True).text,
            'Price': r.html.xpath('//*[@id="priceblock_ourprice"]', first=True).text,
            'Stock': r.html.xpath('//*[@id="availability_feature_div"]', first=True).text
        }
    except:
        product = {
            'Amazon US': r.html.xpath('//*[@id="productTitle"]', first=True).text,
            'Price': 'Unavailable',
            'Stock': '*Out of stock*'
        }

    if product['Stock'] == "*Out of stock*":
        None
    else:
        product['Stock'] = '*In stock*'

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

    print(Fore.BLUE + "[Amazon US]" + "  " +
          "\033[39m" + product["Amazon US"] + "  " + StylizedPrice + "  " + "\033[39m" + StylizedProduct)

    return product


def loopAmazonStock():
    for url in amazon_products:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
        getAmazonStock(url, headers)


loopAmazonStock()
