import scrapy
from crawler_observers.crawler_observer import CrawlerObserver
from crawler_objects.crawler_link import CrawlerLink
from crawler_objects.crawler_broken_link import CrawlerBrokenLink


class ScrapyWebCrawler(scrapy.Spider):
    def __init__(self, seed_url: str, crawler_name: str, observer: CrawlerObserver):
        self.name = crawler_name
        self.start_urls = [seed_url]
        self._observer = observer
        super().__init__()

    def parse(self, response) -> None:
        current_crawler_link = CrawlerLink(response.url, response.meta['depth'])
        self._observer.notify_new_link(current_crawler_link)
        for image in response.xpath('//img/@src').extract():
            image_url = response.urljoin(image)
            self._observer.notify_new_image(current_crawler_link, image_url)
        for link in response.xpath("*//a/@href").extract():
            if link is not None:
                next_page = response.urljoin(link)
                yield scrapy.Request(next_page, callback=self.parse, errback=self.parse_invalid_request)

    def parse_invalid_request(self, failure) -> None:
        link = failure.value.response.url
        depth = failure.value.response.meta['depth']
        status = failure.value.response.status
        self._observer.notify_new_link(CrawlerBrokenLink(link, depth, status))
