import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}

url = "https://www.ptt.cc/bbs/movie/index{}.html"
page = 9500

for i in range(5):
    res = requests.get(url.format(page), headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')

    # print(soup)
    title_tag_list = soup.select('div.title a')
    for title_tag in title_tag_list:
        # print(title_tag)
        title_name = title_tag.text
        title_url = "https://www.ptt.cc" + title_tag['href']
        print(title_name)
        print(title_url)
        print('==============')

    page -= 1