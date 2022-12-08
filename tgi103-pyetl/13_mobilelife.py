import requests
import json
import pprint
from bs4 import BeautifulSoup


url = "https://www.newmobilelife.com/wp-json/csco/v1/more-posts"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

data = {
    "action": "csco_ajax_load_more",
    "page": 4,
    "posts_per_page": 30
}

res = requests.post(url, headers=headers, data=data)

# print(res.text)
json_data = json.loads(res.text)
# pprint.pprint(json_data)
html = json_data["data"]["content"]
# print(html)
soup = BeautifulSoup(html, 'html.parser')
for div in soup.select("div.cs-entry__excerpt"):
    print(div.text)