############################################################################
#
#
# Author: Andrei C. Cojocaru
# Linkedin: https://www.linkedin.com/in/andrei-cojocaru-985932204/
# Facebook: https://www.facebook.com/webautomation.romania
# Tiktok: https://www.tiktok.com/@n0hacker_reporter13
# Twitter: https://twitter.com/andrei_reporter
# Youtube: https://www.youtube.com/channel/UCgx_Y9OHi5KPVzLJo9setxw/featured
# GitHub: https://github.com/andreireporter13
# Website: https://webautomation.ro/
# 
# 
############################################################################

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
        print('Yeah, its work.')
    else: 
        print('No, somethingwrong...')