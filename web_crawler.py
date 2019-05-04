from scrapy.crawler import CrawlerProcess
from scrapy_web_crawler import ScrapyWebCrawler
from crawler_observers.crawler_observer import CrawlerObserver
from configuration.config import Config


class WebCrawler:
    CRAWLER_NAME = "Crawly"

    @classmethod
    def crawl(cls, link: str, observer: CrawlerObserver) -> None:
        crawler_process = CrawlerProcess({'USER_AGENT': Config.AGENT, 'LOG_FILE': Config.SCRAPY_LOG_FILE})
        crawler_process.crawl(ScrapyWebCrawler, link, cls.CRAWLER_NAME, observer)
        crawler_process.start()
