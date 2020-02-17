import requests
from bs4 import BeautifulSoup
from constants import Constants

class Helper:

    @staticmethod
    def get_payload_for_page(page):
        payload = Constants.payloadTemplate % page
        return payload


    @staticmethod
    def get_last_page(soup):
        elements = soup.find_all('div', attrs={"class": 'col-lg-6 col-md-6 col-sm-6 col-xs-6 pagination_container'})
        last_page = elements[1].contents[1].attrs['href'].replace("javascript:p('", '').replace("')", '')
        return last_page

    @staticmethod
    def get_soup(page):
        payload = Helper.get_payload_for_page(page)
        response = requests.request("POST", Constants.url, data=payload, headers=Constants.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup