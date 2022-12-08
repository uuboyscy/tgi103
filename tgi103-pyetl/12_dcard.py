import requests
import json
import pprint
import os

if not os.path.exists("./dcard_photo"):
    os.mkdir("./dcard_photo")

url = "https://www.dcard.tw/service/api/v2/forums/photography/posts?limit=100&before=240574515&__cf_chl_tk=A27tZr2VCp4.1jLwdpm_rrozzhuAqOyA.NgTeuABMZQ-1670462391-0-gaNycGzNCuU"


headers_str = """accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6
cache-control: max-age=0
cookie: dcsrd=iYvYJgaEzDgfzbEiIxDhsEeD; dcsrd.sig=Ngp0dlsS9jMfli3PS_gwwN_3Mcs; __auc=b39d860a173a78efe9a9c4c48f8; G_ENABLED_IDPS=google; __htid=d46865a2-536e-458b-a29d-049bea705f43; _fbp=fb.1.1634373141652.1677113179; cto_bundle=kG54hl9nTDlYeWpWQVVPMUlsdjlJSyUyRlJIRSUyRiUyRm5qaFV1SzlldWRwN1NieiUyQnhjVTJjeU5kUVZSbUpGRFRFcWlHMkJvJTJCaVZaMGklMkZyZnJ5aENIUDhXb3hDNGZXOEt6SGNGS0dzZTFjVEV2MFN5SWowejhQc3VsVDVrSlJ6TFVVVXU4WEwxSVdpR092djJaSUlRck5XWUpESjElMkZ1ZyUzRCUzRA; __cfruid=d6a5b44e92b03d3d261000c6e690ab3ab42ba995-1663400068; __gads=ID=4ca85d7d7cd4cea5:T=1665829772:S=ALNI_MY3k9nsoOhXQ2doMZeu3d2lKCKoRQ; _gcl_au=1.1.693566351.1668930154; _cfuvid=nzhuaRXX5.V2M1x.FZCnfsfMu63D_t2GrJ1ebKpClsE-1670461716049-0-604800000; _gid=GA1.2.680955960.1670461719; _ga=GA1.1.1578877340.1596244033; _ga_C3J49QFLW7=GS1.1.1670461719.63.1.1670461719.0.0.0; __gpi=UID=0000066e7b37fac6:T=1654577378:RT=1670461719:S=ALNI_MbcQIiPl2mE9G0Av--vd53pE4L_zA; cf_chl_2=08c18694a1220de; cf_clearance=R63RxbgSBY8ZQUgVMt0FCy.I12XJR7eQz6tZ9d31tS4-1670462406-0-250
sec-ch-ua: "Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "macOS"
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: none
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"""

headers = {r.split(": ")[0]: r.split(": ")[1] for r in headers_str.split("\n")}

print(headers)

# res = requests.get(url, headers=headers)
# print(res.text)

with open("dcard.json", "r", encoding="utf-8") as f:
    json_str = f.read()

json_data = json.loads(json_str)
print(json_data)
print(type(json_data))

json_data = json.load(open("dcard.json", "r", encoding="utf-8"))
print(json_data)
print(type(json_data))

# for data in json_data:
#     print(data)

# pprint.pprint(json_data[1]['mediaMeta'])

# mediaMeta[n]["url"] title
for article_obj in json_data:
    title_name = article_obj["title"]
    print(title_name)
    for img_obj in article_obj["mediaMeta"]:
        img_url = img_obj["url"]
        print("\t" + img_url)
        res_img = requests.get(img_url)
        img_content = res_img.content
        img_name = img_url.split("/")[-1]
        try:
            with open("./dcard_photo/{}".format(img_name), "wb") as f:
                f.write(img_content)
        except:
            pass
    print("=========")

