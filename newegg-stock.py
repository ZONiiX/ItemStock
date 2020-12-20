from requests_html import HTMLSession

newegg_products = ['https://www.newegg.com/amd-ryzen-5-5600x/p/N82E16819113666?Description=ryzen&cm_re=ryzen-_-19-113-666-_-Product', 'https://www.newegg.com/amd-ryzen-7-5800x/p/N82E16819113665?Description=ryzen%205700&cm_re=ryzen_5700-_-19-113-665-_-Product',
                   'https://www.newegg.com/amd-ryzen-9-5900x/p/N82E16819113664?Description=ryzen%205700&cm_re=ryzen_5700-_-19-113-664-_-Product', 'https://www.newegg.com/amd-ryzen-9-5900x/p/N82E16819113664?Description=ryzen%205700&cm_re=ryzen_5700-_-19-113-664-_-Product', 'https://www.newegg.com/black-msi-gl-series-gl75-10sfk-029-gaming-entertainment/p/N82E16834155401?Item=N82E16834155401&cm_sp=homepage_dailydeals-_-p2_34-155-401-_-12192020&quicklink=true']


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
        None
    else:
        product['Stock'] = 'In Stock'

    print(product)

    return product


for url in newegg_products:
    getNeweggStock(url)
