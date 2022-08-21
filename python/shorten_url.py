# https://www.shorturl.at

# long_url = https://www.lemonde.fr/series-d-ete/article/2022/08/12/surf-yoga-et-fiesta-des-packages-qui-gagnent-le-c-ur-d-une-jeunesse-urbaine-et-diplomee_6137836_3451060.html
# short_url = shorturl.at/BDT29

# python3 shoturl.py -u [URL_Long]
import argparse
import requests
from bs4 import BeautifulSoup

API_URL = "https://www.shorturl.at/shortener.php"

class API:

    __url = ""
    __short_url = ""

    def __init__(self):
        pass

    def set_url(self, url):
        self.__url = url
    
    def get_short_url(self):
        return self.__short_url
    
    def request_short_url(self):
        payload = {'u':self.__url}
        try:
            r = requests.post(API_URL, data=payload)
        except:
            print("[-] request error\n")
            return -1

        #print(r.text)
        return r.text
    
    def extract_data_from_html(self, html_text):
        bs = BeautifulSoup(html_text, 'html.parser')
        input_tag = bs.find("input", attrs={'id': 'shortenurl'})

        try:
            self.__short_url = input_tag.attrs["value"]
            #print(input_tag.attrs["value"])
        except:
            print("[-] extraction error\n")
            return -1

def main(url):
    if url == "" or url is None:
        url = input("Input URL")
    else:
        print(url)
    #pass

    api = API()
    api.set_url(url)
    html_text = api.request_short_url()
    
    if api.extract_data_from_html(html_text) == -1:
        #print()
        exit(1)
    
    
    print(api.get_short_url())



parser = argparse.ArgumentParser("URL Shortener")

parser.add_argument('-u', '--url', help="URL")

args = parser.parse_args()

main(args.url)