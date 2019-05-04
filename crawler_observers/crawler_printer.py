from crawler_observers.crawler_observer import CrawlerObserver
from crawler_objects.crawler_link import CrawlerLink
from crawler_objects.crawler_image_references import CrawlerImageReferences


class CrawlerPrinter(CrawlerObserver):
    def __init__(self):
        self._image_src_to_crawler_image_references = dict()

    def notify_new_link(self, crawler_link: CrawlerLink) -> None:
        print(str(crawler_link))

    def notify_new_image(self, referrer: CrawlerLink, image_src: str) -> None:
        if image_src not in self._image_src_to_crawler_image_references:
            self._image_src_to_crawler_image_references[image_src] = CrawlerImageReferences(image_src)
        crawler_image_references = self._image_src_to_crawler_image_references[image_src]
        crawler_image_references.add_referrer(referrer)
        if len(crawler_image_references) > 1:
            print(self._image_src_to_crawler_image_references[image_src])
