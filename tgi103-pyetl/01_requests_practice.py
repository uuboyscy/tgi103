import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}

# url = "https://9b48-35-78-89-85.ngrok.io/hello_get?name=allen"
url = "https://www.ptt.cc/bbs/joke/index.html"

res = requests.get(url, headers=headers)

print(res.text)
