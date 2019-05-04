class CrawlerLink:
    def __init__(self, link: str, depth: int):
        self._link = link
        self._depth = depth

    def __str__(self):
        return """
        url: {url} --> depth: {depth}
        """.format(url=self._link, depth=self._depth)
