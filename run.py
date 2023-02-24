import requests
from bs4 import BeautifulSoup
import sys
from urllib.parse import urljoin

# Starting new session
s = requests.Session()

s.headers["User-Agent"] = '''Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'''
# This functions returns all the forms in a given url
def get_forms(url):
    soup = BeautifulSoup(s.get(url).content, "html.parser")
    return soup.find_all("form")

def form_information(form):
    form_info = {}
    action = form.attrs.get("action")
    method = form.attrs.get("method", "get")
    input_tags = []

    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        input_value = input_tag.attrs.get("value", '')

        input_tags.append({
            "type": input_type,
            "name": input_name,
            "value": input_value
        })

    form_info["action"] = action
    form_info["method"] = method
    form_info["input_tags"] = input_tags
    return form_info


    def vulnerability_scanner(response):
        for error in errors:
            if error in response.content.decode().lower():
                return True
        return False


