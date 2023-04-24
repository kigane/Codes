import hashlib
import aiohttp
import asyncio
from rich import print
import requests

comicID = 28241
sessdata = "6b5090fe,1697711767,8b770*42"
BASE_URL = 'https://manga.bilibili.com/twirp/comic.v1.Comic/ComicDetail?device=pc&platform=web'
payload = {"comic_id": comicID}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56',
    'origin': 'https://manga.bilibili.com',
    'referer': f'https://manga.bilibili.com/detail/mc{comicID}?from=manga_homepage',
    'cookie': f'SESSDATA={sessdata}'
}

url = 'https://manga.hdslb.com/bfs/manga/3168f025ec1d676626532ade12b1b55a7ca7fea6.jpg?token=18858cb1388bf7760370101190541669&ts=64463086'

resp = requests.get(url)
md5code = hashlib.md5(resp.content).hexdigest()
# print(resp.headers['Etag'])

async def main():
    async with aiohttp.ClientSession() as session:
        # async with session.post(BASE_URL, data=payload, headers=headers) as resp:
        #     print(resp.status)
        #     rep = await resp.read()
        async with session.get(url) as resp:
            print(resp.ok)
            print(resp.status)
            ret = await resp.read()
            # tag = hashlib.md5(resp.content).hexdigest()
            key = hashlib.md5(ret).hexdigest()
            print(key)
            print(md5code)
            # print(tag)

asyncio.run(main())

