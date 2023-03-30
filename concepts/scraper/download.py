import urllib.request as request
from urllib.request import urlretrieve

import requests

my_headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
]

print("hello")
proxies = {
    'https': 'https://127.0.0.1:8603',  # 查找到你的vpn在本机使用的https代理端口
    'http': 'http://127.0.0.1:8603',  # 查找到vpn在本机使用的http代理端口
}

cookies = {
    "amplitude_idpatreon.com": "meUlkIjozLCJzZXF1ZW5jZU51bWJlciI6M30=",
    "patreon_device_id": "ea046a74-6a0b-49ce-a98e-683f2d44fdad",
}
url = "https://www.patreon.com/file?h=41865063&i=6396286"
opener = request.build_opener(request.ProxyHandler(proxies))
request.install_opener(opener)
ret = requests.get(
    url, headers={"User-Agent": my_headers[0]}, cookies=cookies, proxies=proxies)
print(ret.status_code)  # 403
print(ret.headers)

# urlretrieve(url, 'downloads/21.zip')
