import newspaper
from newspaper import Article

class TextScraper(object):

    def __init__(self, url):
        self.url = url
        self.article = Article(self.url)

    def scrape(self):
        text = ''
        try:
            self.article.download()
            self.article.parse()
            text = self.article.text.replace('\n', '')
        except newspaper.article.ArticleException:
            pass

        return text
    


