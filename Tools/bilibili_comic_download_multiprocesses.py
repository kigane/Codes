import argparse
import asyncio
import os
import shutil
from rich import print
from rich.table import Table
from rich.console import Console
from rich.progress import Progress, track
import requests
import datetime
import time
from retry import retry
import threading
import json
import hashlib

from concurrent.futures import ThreadPoolExecutor, as_completed, ProcessPoolExecutor

console = Console()


def _time():
    t = datetime.datetime.fromtimestamp(time.time())
    timeStr = t.strftime("[ %Y.%m.%d %H:%M:%S ]")
    return "[rgb(102, 102, 153)]%s[/]" % timeStr


def info(msg):
    timeStr = _time()
    logStr = "%s [b]|[rgb(51, 204, 204)]INFO[/]|[/b] %s" % (timeStr, msg)
    print(logStr)


def error(msg):
    timeStr = _time()
    logStr = "%s [b]|[rgb(204, 0, 0)]ERROR[/]|[/b] %s" % (timeStr, msg)
    print(logStr)


def isInt(a):
    try:
        int(a)
        return True
    except:
        return False


def ceil(num):
    if isinstance(num, (float,)):
        return int(num) + 1
    else:
        return num


class Episode:
    """
        一集
    """

    def __init__(self, jsonData, sessData, comicID):
        self.id = jsonData['id']
        self.available = not jsonData['is_locked']
        self.ord = jsonData['ord']  # 真正的顺序..
        # 使用short_title作为显示/标注用的标题
        self.title = jsonData['short_title']
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56',
            'origin': 'https://manga.bilibili.com',
            'referer': f'https://manga.bilibili.com/detail/mc{comicID}/{self.id}?from=manga_homepage',
            'cookie': f'SESSDATA={sessData}'
        }
        self.rootPath = './data/' + str(comicID) + f'/{self.ord}'
        if not os.path.exists(self.rootPath):
            os.mkdir(self.rootPath)

    def getAvailable(self):
        return self.available

    @retry(delay=1)
    def downloadImg(self, token, url, index):
        url = url + "?token=" + token
        file = requests.get(url)
        
        if file.headers['Etag'] != hashlib.md5(file.content).hexdigest():
            error(f"下载内容校验和不正确! {file.headers['Etag']} ≠ {hashlib.md5(file.content).hexdigest()}")
            # raise Exception

        # 下载图片
        with open(os.path.join(self.rootPath, f"{index}.jpg"), 'wb') as f:
            f.write(file.content)

        return os.path.join(self.rootPath, f"{index}.jpg")

    def download(self):
        url = 'https://manga.bilibili.com/twirp/comic.v1.Comic/GetImageIndex?device=pc&platform=web'
        payloads = {
            'ep_id': self.id
        }
        if os.path.isdir(self.rootPath) and len(os.listdir(self.rootPath)) > 0:
            # 相同文件名已经存在 跳过下载
            return
        # 获取一话中的所有图片在内部的位置
        rep = requests.post(url, data=payloads, headers=self.headers)
        if rep.ok:
            data = rep.json()
            images = data['data']['images']
            paths = []
            for img in images:
                paths.append(img['path'])
            payloads = {
                "urls": json.dumps(paths)
            }
            url = "https://manga.bilibili.com/twirp/comic.v1.Comic/ImageToken?device=pc&platform=web"

            @retry(delay=1)
            def _():
                return requests.post(url, data=payloads, headers=self.headers)
                
            # 获取每张图片的实际url和token
            rep = _()
            if rep.ok:
                i = 1
                for img in rep.json()['data']:
                    self.downloadImg(img['token'], img['url'], i)
                    i += 1

class Comic:
    """
        一个漫画
    """

    def __init__(self, comicID: int, sessdata: str, args) -> None:
        # 初始化
        if len(sessdata) == 0:
            self.sessdata = False
        else:
            self.sessdata = sessdata
        info(f'初始化漫画 ID {comicID}')
        self.id = comicID
        self.start = args.start
        self.end = args.end
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56',
            'origin': 'https://manga.bilibili.com',
            'referer': f'https://manga.bilibili.com/detail/mc{comicID}?from=manga_homepage',
        }
        if self.sessdata:
            self.headers.update({'cookie': f'SESSDATA={self.sessdata}'})

        self.detailUrl = 'https://manga.bilibili.com/twirp/comic.v1.Comic/ComicDetail?device=pc&platform=web'
        self.threads = args.threads

        # 属性
        self.title = 'Nope'
        self.authorName = []
        self.styles = []
        self.evaluate = 'Nope'
        self.total = 0
        self.episodes = []
        self.success = False

    def fetch(self):
        @retry()
        def mkdir():
            os.mkdir(f'./data/{self.id}')
        if not os.path.exists('./data'):
            os.mkdir('./data')
        if os.path.exists(f'./data/{self.id}'):
            if os.path.isdir(f'./data/{self.id}'):
                info('存在历史下载 将避免下载相同文件!')
            else:
                os.remove(f'./data/{self.id}')
                mkdir()
        else:
            mkdir()


        payload = {"comic_id": self.id}
        with console.status('正在访问BiliBili Manga'):
            rep = requests.post(self.detailUrl, data=payload, headers=self.headers)
        if rep.ok:
            info('漫画信息GET XD')
            info('开始解析信息...')
            # try:
            data = rep.json()
            self.analyzeData(data)
            # 开始爬取
            with console.status("[grenn]Downloading"), ProcessPoolExecutor(max_workers=8) as pool:
                # fan-out. 用类的实例方法作map的参数应该要手动绑定方法。
                # task = progress.add_task("Download episodes", total=len(self.episodes))
                for _ in pool.map(Episode.download, self.episodes):
                    # progress.advance(task, 1)
                    pass
                # auto fan-in

            info('任务完成!')

        else:
            error('请求错误 / 网络错误!')
            error(f'详细信息: {rep.status_code}')
            error("请检查输入信息是否正确!")

    def analyzeData(self, data):
        if data['code'] != 0:
            error(f'漫画信息有误! 请仔细检查! (提示信息{data["msg"]})')
            return False

        self.title = data['data']['title']
        self.authorName = data['data']['author_name']
        self.styles = data['data']['styles']
        self.evaluate = data['data']['evaluate']
        self.total = data['data']['total']
        t = Table(title='漫画作品详情')
        t.add_column('[green bold]作品标题[/green bold]')
        t.add_column('[green bold]作者[/green bold]')
        t.add_column('[green bold]标签[/green bold]')
        t.add_column('[green bold]概要[/green bold]')
        t.add_column('[green bold]总章节[/green bold]')
        t.add_row(self.title, ', '.join(self.authorName),
                  ''.join(self.styles), self.evaluate, str(self.total))
        self.episodes = []
        self.ordTitle = {}
        console.print(t)
        _from = self.start
        _to = self.end
        if _to is None:
            # 不输入则不限制
            _to = 999999999
        # 允许小于等于才能够下载单章以及输入两个0下载全部
        assert _from <= _to

        # with open('debug.json', 'wb') as f:
        #     f.write(json.dumps(data))
        with console.status('正在解析详细章节...'):
            epList = data['data']['ep_list']
            epList.reverse()
            for episode in epList:
                if _from <= episode['ord'] <= _to:
                    # BiliBili漫画索引号是反着的
                    epi = Episode(episode, self.sessdata, self.id)
                    if epi.getAvailable():
                        self.episodes.append(epi)
                        self.ordTitle[epi.ord] = epi.title

                if (not bool(_from)) and (not bool(_to)): # 输入0,0爬取全部
                    epi = Episode(episode, self.sessdata, self.id)
                    if epi.getAvailable():
                        self.episodes.append(epi)
                        self.ordTitle[epi.ord] = epi.title

        info(f'分析结束 将爬取章节数: {len(self.episodes)}/{self.total} 准备开始爬取!')
        return True

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--id', default='30460', type=str, help='https://manga.bilibili.com/detail/mc{comicID} 漫画主页网址的最后几个数字')
    parser.add_argument('--sessdata', default="", type=str, help='付费漫画需要的cookie')
    # 30460
    parser.add_argument('--threads', default=8, type=int, help='最大线程数')
    parser.add_argument('--start', default=0, type=int, help='需要下载的起始章节')
    parser.add_argument('--end', default=0, type=int, help='需要下载的结束章节。0->0表示全下')
    args, _ = parser.parse_known_args()

    # comicID = args.id
    comicID = 28241
    sessdata = "6b5090fe,1697711767,8b770*42"
    args.start = 0
    args.end = 13
    c = Comic(comicID, sessdata, args)
    fetch_start = time.time()
    c.fetch()
    fetch_end = time.time()
    info(f'结束: 耗时 {fetch_end - fetch_start} s')

    # 8 threads asyncio 86s
    # 8 threads no asyncio 86s
    # 8 process no asyncio 51s
