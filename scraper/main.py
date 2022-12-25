import requests
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>

<p>
<a href="http://example.com/elsie" id="link1">Elsie</a>or
<a href="http://example.com/lacie" id="link2">Lacie</a> and
<a href="http://example.com/tillie" id="link3">Tillie</a>;
lived at the bottom of a well.
</p>

<p class="story">...</p>
</body>
</html>
"""

# soup = BeautifulSoup(html_doc, 'lxml')

# ret = soup.find(text='Elsie')
import pandas as pd
url='https://brotato.wiki.spellsandguns.com/Items'
df=pd.read_html(url)[0] 
# [0]：表示第一个table，多个table需要指定，如果不指定默认第一个
print(df)

# print(type(ret.strings))
# print([type(e) for e in list(ret.children)])

# help(soup.find)
