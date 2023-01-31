import re
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from icecream import ic
from url_manager import UrlManager

ic.configureOutput(prefix=lambda: datetime.now().strftime('%H:%M:%S | '),
                   includeContext=False)

proxies = {
    'https': 'https://127.0.0.1:8603',  # 查找到你的vpn在本机使用的https代理端口
    'http': 'http://127.0.0.1:8603',  # 查找到vpn在本机使用的http代理端口
}

headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"
}

cookies = {
    "amplitude_idpatreon.com": "meUlkIjozLCJzZXF1ZW5jZU51bWJlciI6M30=",
    "patreon_device_id": "ea046a74-6a0b-49ce-a98e-683f2d44fdad",
    "patreon_locale_code": "zh-CN",
    "_ALGOLIA": "anonymous-31114cbc-2ffc-43d5-9c8c-b28049deb31e",
    "amplitude_idpatreon.com":  "eyJkZXZpY2VJZCI6IjdmNmM5M2JkLTkyYmItNGQxZS05ZWIwLTVlMzI1ZmI3YzcwZCIsInVzZXJJZCI6bnVsbCwib3B0T3V0IjpmYWxzZSwic2Vzc2lvbklkIjoxNjYyMjEzNTE2NzY2LCJsYXN0RXZlbnRUaW1lIjoxNjYyMjEzNTYyMTExLCJldmVudElkIjowLCJpZGVudGlmeUlkIjozLCJzZXF1ZW5jZU51bWJlciI6M30=",
    "G_ENABLED_IDPS": "google",
    "session_id": "zKZVHwWvD7MQROB8w03bFbca-K2C5AfsE4VDlk1c5cA",
    "patreon_location_country_code": "CN",
    "__cf_bm": "SwB4ToghQa0xlpbFhHPxptF7ArkAMdJ9e9KcPRB6Y3Y-1673933920-0-AZN5bTsGSlmjoADY2L7jzjiSyXY9TlopYyUW+m90nfKG0TXyVqfnlvUvHpYOUaLh/n59rXU8osU/LNiY+VgzO7rHI1FTuE7pApilrjso+5XW",
    "datadome": "7hb5qST3~8dkk~Z25~TE4VW6L0jCjfGMs4CdwSZ5nuztW8MunS1UfoPYN3bUD5NzQ-qW63PAWa9e6GIWZyUYA-7L-wlkoWmCLuDi3_LU80hB0lXt8kM~I~1B66ZsLgL-"
}

if __name__ == '__main__':
    code_urls = []
    d_urls = []
    url_manager = UrlManager()
    base_url = "https://sebastiangraves.com/create-dark-souls-in-unity/"
    ret = requests.get(base_url)
    ic(ret.status_code)
    ic(ret.headers)
    soup = BeautifulSoup(ret.content, 'html.parser')
    links = soup.find_all('a')
    # t = 'Episode 46 – “LOOTABLE CHESTS”'
    # ret = re.match("Episode (\d+)", t)
    # ic(ret.group(1))
    for link in links:
        ret = re.match("Episode (\d+)", link.text)
        if ret and int(ret.group(1)) > 20:
            d_urls.append(link['href'])

    while len(d_urls) > 0:
        mid_url = d_urls.pop(0)
        ic(mid_url)
        ret = requests.get(mid_url)
        ic(ret.status_code)
        ic(ret.headers)
        soup = BeautifulSoup(ret.content, 'html.parser')
        links = soup.find_all('a')
        download_page = ''
        for link in links:
            ret = re.match(
                "https://www.patreon.com/posts/(\d+)", link["href"])
            if ret:
                download_page = link['href']
                break

        code_urls.append(download_page) 
    print(code_urls)
