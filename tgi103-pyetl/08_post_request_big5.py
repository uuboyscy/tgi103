import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}

url = "https://organic.afa.gov.tw/InOrganic/QueryApplyList"

data = {
    "TYPE": "1",
    "YEAR": "111",
    "qNnify_NO": "",
    "qC_NAME": "",
    "qPaper_NO": "",
    "qProduct_NAME": "米".encode("big5"),
    "B": "查　　詢"
}

res = requests.post(url, data, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

# print(res.text)
for tr_obj in soup.select('table table tr')[7:]:
    com_name = tr_obj.select('td')[0].text
    tel_no = tr_obj.select('td')[1].text
    case_no = tr_obj.select('td')[2].text.replace("\n", "")
    print("Company Name:\t", com_name)
    print("Telephone No.:\t", tel_no)
    print("Case No.:\t", case_no)
    print("==========")