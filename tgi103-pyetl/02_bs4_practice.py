import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}

# url = "https://9b48-35-78-89-85.ngrok.io/hello_get?name=allen"
url = "https://www.ptt.cc/bbs/joke/index.html"

res = requests.get(url, headers=headers)  # To get Response object (include HTML string)

soup = BeautifulSoup(res.text)
# print(soup)

# logo_obj = soup.findAll('a', {'id': 'logo'})[0]
logo_obj = soup.findAll('a', id='logo')[0]
# logo_obj = soup.findAll('a')
print(logo_obj)
print(logo_obj.text)
print("https://www.ptt.cc" + logo_obj['href'])

print("=========")

board_obj = soup.findAll('a', class_='board')
board_obj = soup.select('a[class="board"]')
board_obj = soup.select('a.board')  # Return a list of Tag

print(board_obj)

board = board_obj[0].find('span')  # Return a Tag
print(board)
print(type(soup))
print(type(board_obj[0]))


