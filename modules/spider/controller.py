from modules.config.config import START_URL
from .spider import Spider


class SpiderController(object):
    def __init__(self, url):
        self.url = url

    def start_spider(self):
        crawled_data = Spider(url=self.url)