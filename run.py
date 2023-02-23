import requests
from bs4 import BeautifulSoup
import sys
from urllib.parse import urljoin

# Starting new session
s = requests.Session()

s.headers["User-Agent"] = '''
                            Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) 
                            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36
                            '''

def get_forms(url):
    soup = BeautifulSoup(s.get(url).content, "html.parser")
    return soup.find_all("form")