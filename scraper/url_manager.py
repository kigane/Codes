from icecream import ic


class UrlManager():
    def __init__(self) -> None:
        self.new_url = set()
        self.old_url = set()

    def add_url(self, url):
        if url is None or len(url) == 0:
            ic("无效的url")
            return

        if url in set.union(self.new_url, self.old_url):
            ic("重复的url")
            return

        self.new_url.add(url)

    def add_urls(self, urls):
        if urls is None or len(urls) == 0:
            ic("无效的urls")
            return

        for url in urls:
            self.add_url(url)

    def has_new_url(self):
        return len(self.new_url) > 0

    def get_url(self):
        if self.has_new_url():
            url = self.new_url.pop()
            self.old_url.add(url)
            return url
        else:
            return None
