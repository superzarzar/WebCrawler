from typing import List
from crawler_objects.crawler_link import CrawlerLink


class CrawlerImageReferences:
    def __init__(self, image_src: str):
        self._image_source = image_src
        self._referrers: List[CrawlerLink] = []

    def add_referrer(self, referrer: CrawlerLink):
        self._referrers.append(referrer)

    def __str__(self):
        return """
        image_src: {image_source},
        referrers: {referrers}
        """.format(image_source=self._image_source, referrers=[str(referrer) for referrer in self._referrers])

    def __len__(self):
        return len(self._referrers)
