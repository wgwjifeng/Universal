from scrapy.link import Link
from scrapy.utils.python import unique as unique_list, to_native_str
from scrapy.utils.response import get_base_url
import re

class RegexLinkExtractor():
    def __init__(self, restrict_re='', base_url=None):
        self.restrict_re = restrict_re
        self.base_url = base_url
    
    def extract_links(self, response):
        if not self.base_url:
            self.base_url = get_base_url(response)
        items = re.findall(self.restrict_re, response.text)
        all_links = [Link(response.urljoin(self.base_url.format(str(item)))) for item in items]
        return unique_list(all_links)
