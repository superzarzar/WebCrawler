from crawler_objects.crawler_link import CrawlerLink


class CrawlerBrokenLink(CrawlerLink):
    def __init__(self, link: str, depth: int, status_code: int):
        super().__init__(link, depth)
        self._status_code = status_code

    def __str__(self):
        return "{link_str} --> status code: {status_code}".format(link_str=super().__str__(),
                                                                  status_code=self._status_code)
