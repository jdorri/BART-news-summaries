import newspaper
from newspaper import Article

class TextScraper(object):
    """
    A class for scraping text from a webpage
    with the (free) Python newspaper library.

    See https://newspaper.readthedocs.io/en/latest/index.html
    for more information. 

    Args:
        url (str): http address
        article (Article): instantiated Article object
    """

    def __init__(self, url):
        self.url = url
        self.article = Article(self.url)

    def scrape(self):
        """
        Scrapes the text.

        Returns:
            text (str): the full article 
        """
        text = ''
        try:
            self.article.download()
            self.article.parse()
            text = self.article.text.replace('\n', '')
        except newspaper.article.ArticleException:
            pass

        return text
    


