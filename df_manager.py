import pandas as pd 

from text_scraper import TextScraper
from nlp_tasks import NLP

class DataFrameManager(object):
    """
    A class for creating a "news dataframe" from
    the raw JSON-formatted response data. Simplifies 
    data access for downstream NLP tasks.
    """

    def __init__(self):
        pass

    def make_df(self, news, query):
        """
        Makes the Pandas dataframe. 

        Args:
            news (NewsAPI): reponse object
            query (str): company/person 
        Returns:
            df (Dataframe): news dataframe 
        """
        rows = self.make_rows_from_json(news, query)
        col_names = ['Publisher', 'Title', 'URL', 'Image URL', 'Date', 'Scrape', 'BART', 'NE_1']

        df = pd.DataFrame(rows, columns=col_names)
        return df 

    @staticmethod
    def make_rows_from_json(news, query):
        """
        Peforms the JSON-to-rows conversion.

        Args:
            news (NewsAPI): reponse object
        Returns:
            rows (list): each element is 
            a list containing data for the
            frontend, one for each article
        """
        rows = []
        if news['articles'] != []:
            for article in news['articles']:
                publisher = article['source']['Name']
                title = article['title']
                url = article['url']
                image_url = ''#article['urlToImage']
                date = article['publishedAt']
                
                scraper = TextScraper(url)
                scrape = scraper.scrape()

                nlp = NLP()
                if scrape == '':
                    BART = 'Not available...'
                else:
                    BART = nlp.summarise_with_BART(scrape)

                key_ent = nlp.NER_with_SpaCy(scrape, query)
                ent_1 = key_ent[0][0] 
                
                row = [publisher, title, url, image_url, date, scrape, BART, ent_1]
                rows.append(row)

        return rows



