from requests_html import HTMLSession

amazon_products = ['https://www.amazon.com/AMD-Ryzen-5600X-12-Thread-Processor/dp/B08166SLDF?ref_=ast_sto_dp', 'https://www.amazon.com/AMD-Ryzen-5800X-16-Thread-Processor/dp/B0815XFSGK?ref_=ast_sto_dp',
                   'https://www.amazon.com/Ryzen-5900X-12-Core-Desktop-Processor/dp/B08NXYLBN5/ref=sr_1_3?dchild=1&keywords=ryzen+9+5900x&qid=1608348416&s=electronics&sr=1-3', 'https://www.amazon.com/AMD-Ryzen-5950X-32-Thread-Processor/dp/B0815Y8J9N?ref_=ast_sto_dp']


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
            'Stock': 'Out of stock'
        }

    print(product)

    return product

def loopAmazonStock():
        for url in amazon_products:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
            getAmazonStock(url, headers)
