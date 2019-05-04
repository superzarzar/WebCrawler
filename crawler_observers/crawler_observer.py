from abc import ABC, abstractmethod
from crawler_objects.crawler_link import CrawlerLink


class CrawlerObserver(ABC):
    @abstractmethod
    def notify_new_link(self, crawler_link: CrawlerLink) -> None:
        pass

    @abstractmethod
    def notify_new_image(self, referrer: CrawlerLink, image_src: str) -> None:
        pass
