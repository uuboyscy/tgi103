import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}
url = "https://9b48-35-78-89-85.ngrok.io/hello_post"
url = "http://httpbin.org/post"

data = {
    "username": "Allen"
}

res = requests.post(url, headers=headers, data=data)
res = requests.post(url, data=data)

print(res.text)