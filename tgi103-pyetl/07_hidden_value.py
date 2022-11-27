import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}
url = "https://testselect.uuboyscy.repl.co/"

res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')

input_tags = soup.select('input[type="hidden"]')

print(input_tags)
data = dict()

for input_tag in input_tags:
    data[input_tag['name']] = input_tag['value']

print(data)
