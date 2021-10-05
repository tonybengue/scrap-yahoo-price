# tuto : https://www.youtube.com/watch?v=VLFT65xX8Qw
# todo: https://youtu.be/_Bu6povAuSU

from bs4 import BeautifulSoup
import requests
import time

from colors import Colors
    
def main():
    stock = 'TSLA'
    url = 'https://fr.finance.yahoo.com/quote/' + stock
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    nbRequests = 0
    timeToSleep = 5 # seconds

    while True:
        page = requests.get(url, headers = headers)
        
        soup = BeautifulSoup(page.text, 'lxml')
        #print(soup)
        
        price = soup.find('span', class_ = 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)').text
        priceEarn = soup.find('span', class_ = 'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)').text
        
        nbRequests += 1
        print(
            'Request: ' + str(nbRequests) + ' for stock ' + Colors.OKGREEN + stock + Colors.ENDC, price, priceEarn
        )
        time.sleep(timeToSleep)

if __name__ == "__main__":
    main()