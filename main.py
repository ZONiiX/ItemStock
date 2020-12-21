import multiprocessing
from amazon_stock import loopAmazonStock
from newegg_stock import loopNeweggStock

if __name__ == '__main__':
    while(True):
        p1 = multiprocessing.Process(target=loopAmazonStock)
        p2 = multiprocessing.Process(target=loopNeweggStock)

        p1.start()
        p2.start()

        p1.join()
        p2.join()
