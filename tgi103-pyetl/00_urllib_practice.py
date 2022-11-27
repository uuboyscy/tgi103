from urllib import request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}

# url = "https://9b48-35-78-89-85.ngrok.io/hello_get?name=allen"
url = "https://www.ptt.cc/bbs/joke/index.html"

# res = request.urlopen(url=url)
req = request.Request(url=url, headers=headers)
res = request.urlopen(req)

html = res.read().decode("utf-8")

print(html)
