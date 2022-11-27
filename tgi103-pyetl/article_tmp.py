import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}

title_url = "https://www.ptt.cc/bbs/movie/M.1669479836.A.0F9.html"

res_article = requests.get(title_url, headers=headers)
soup_article = BeautifulSoup(res_article.text, 'html.parser')
article_content = soup_article.select_one('div[id="main-content"]').text.split('※ 發信站:')[0]
article_tag = soup_article.select_one('div[id="main-content"]')
for tag in ['div', 'span']:
    for tag_obj in article_tag.select(tag):
        tag_obj.extract()
article_content = article_tag.text
print(article_content)
