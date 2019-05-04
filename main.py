from configuration.config import Config
from web_crawler import WebCrawler
from crawler_observers.crawler_printer import CrawlerPrinter


if __name__ == '__main__':
    WebCrawler.crawl(Config.SEED_URL, CrawlerPrinter())
