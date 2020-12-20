import multiprocessing
from amazon_stock import getAmazonStock, amazon_products, loopAmazonStock
from newegg_stock import getNeweggStock, newegg_products, loopNeweggStock

processes = []
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
'''
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=loopAmazonStock)
    p2 = multiprocessing.Process(target=loopNeweggStock)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
'''
loopAmazonStock()
loopNeweggStock()