from requests import get
from bs4 import BeautifulSoup
from modules.utils.utils import determine_mime_type


class Spider(object):

    def __init__(self, url):
        self.url = url
        self.extracted = {}

    def process_html(self, content):
        extracted = {}

        soup = BeautifulSoup(content, "lxml")
        extracted["links"] = []

        # Get all links
        for link in soup.find_all("a"):
            if link.has_key("href"):
                extracted["links"].append(link.get('href'))

        # TODO: get meta information
        # for link in soup.find_all("meta"):
        #    if link.has_key("href"):
        #        extracted["links"].append(link.get('href'))

        extracted["url"] = self.url
        extracted["content"] = content

        return extracted

    def parse_text(self, content):
        extracted = {"url": self.url, "content": content}
        return extracted

    def run(self):
        resp = get(self.url)
        if resp.status_code == 200:
            content = resp.content
            mime_type = determine_mime_type(content)
            # TODO: Add specific mime types
            if mime_type == "text/html":
                self.extracted = self.process_html(content)
            elif mime_type == "text/plain":
                self.extracted = self.parse_text(content)
            else:
                self.extracted["url"] = self.url

            self.extracted["content-type"] = mime_type.split("/")[1]

            return self.extracted
