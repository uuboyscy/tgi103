import os

import requests
from bs4 import BeautifulSoup

if not os.path.exists("./ptt"):
    os.mkdir("./ptt")

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}

url = "https://www.ptt.cc/bbs/movie/index.html"

for i in range(5):
    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')

    # print(soup)
    # Get all article titles and urls
    title_tag_list = soup.select('div.title a')
    for title_tag in title_tag_list:
        # print(title_tag)
        title_name = title_tag.text
        title_url = "https://www.ptt.cc" + title_tag['href']

        # Extract articles string
        res_article = requests.get(title_url, headers=headers)
        soup_article = BeautifulSoup(res_article.text, 'html.parser')
        # article_content = soup_article.select_one('div[id="main-content"]').text.split('※ 發信站:')[0]
        article_tag = soup_article.select_one('div[id="main-content"]')
        for tag in ['div', 'span']:
            for tag_obj in article_tag.select(tag):
                # Drop the tags we don't want
                tag_obj.extract()
        article_content = article_tag.text

        # Save each article
        try:
            with open("./ptt/{}.txt".format(title_name), "w", encoding="utf-8") as f:
                f.write(article_content)
        except FileNotFoundError as e:
            with open("./ptt/{}.txt".format(title_name.replace("/", "-")), "w", encoding="utf-8") as f:
                f.write(article_content)
        except OSError as e:
            print(e)
        except Exception as e:
            print(e)

        print(title_name)
        print(title_url)
        print('==============')

    # <a class="btn wide" href="/bbs/movie/index9499.html">‹ 上頁</a>
    url = "https://www.ptt.cc" + soup.select('a[class="btn wide"]')[1]['href']
