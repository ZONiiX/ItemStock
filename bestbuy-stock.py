from requests_html import HTMLSession

bestbuy_products = ['https://www.bestbuy.com/site/amd-ryzen-5-5600x-4th-gen-6-core-12-threads-unlocked-desktop-processor-with-wraith-stealth-cooler/6438943.p?skuId=6438943', 'https://www.bestbuy.com/site/amd-ryzen-7-5800x-4th-gen-8-core-16-threads-unlocked-desktop-processor-without-cooler/6439000.p?skuId=6439000',
                    'https://www.bestbuy.com/site/amd-ryzen-9-5900x-4th-gen-12-core-24-threads-unlocked-desktop-processor-without-cooler/6438942.p?skuId=6438942', 'https://www.bestbuy.com/site/amd-ryzen-9-5950x-4th-gen-16-core-32-threads-unlocked-desktop-processor-without-cooler/6438941.p?skuId=6438941']


def getBestBuyStock(url, header):
    s = HTMLSession()
    r = s.get(url, headers=header)
    r.html.render()

    product = {
        'BestBuy US': r.html.xpath('//*[@id="shop-product-title-df9d57b5-a972-4532-8736-6c51cd2ea6d2"]/div', first=True).text,
        'Price': r.html.xpath('//*[@id="pricing-price-70510355"]/div/div/div/div/div[2]/div[1]/div/div/span[1]', first=True).text,
        'Stock': r.html.xpath('//*[@id="fulfillment-add-to-cart-button-a892a694-91db-4f12-a028-c7d424697bd9"]/div/div/div/button', first=True).text
    }

    print(product)

    return product


for url in bestbuy_products:
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    getBestBuyStock(url, header)
