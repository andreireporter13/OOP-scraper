# here I will make a OOP scraper with bs4
#
import requests 
from bs4 import BeautifulSoup 

from fake_useragent import UserAgent


# create class for scraping data
class ScrapData:
    

    def __init__(self, url, headers): 
        self.url = url 
        self.headers = {'UserAgent': headers}

    
    def make_request(self):
        response = requests.get(self.url, headers=self.headers)

        if response:
            return 'Requests succesfuly!'
        else: 
            return 'Requests failed!'


if __name__ == "__main__":

    scraper = ScrapData('https://webautomation.ro', UserAgent().random)
    
    if scraper.make_request():
        print('Eee, merge.')
    else: 
        print('No, ceva nu a mers.')