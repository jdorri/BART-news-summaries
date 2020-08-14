import pandas as pd 

from text_scraper import TextScraper
from nlp_tasks import NLP

class DataFrameManager(object):

    def __init__(self):
        pass

    @staticmethod
    def make_rows_from_json(news, query):
        rows = []
        for article in news['articles']:
            publisher = article['source']['name']
            title = article['title']
            url = article['url']
            image_url = article['urlToImage']
            date = article['publishedAt']
            
            scraper = TextScraper(url)
            scrape = scraper.scrape()

            nlp = NLP()

            if scrape == '':
                BART = 'Not available...'
            else:
                BART = nlp.summarise_with_BART(scrape)

            key_ents = nlp.NER_with_SpaCy(scrape, query)
            ent_1 = key_ents[0][0] 
            ent_2 = key_ents[1][0]
            
            row = [publisher, 
                    title, 
                    url, 
                    image_url, 
                    date,
                    scrape,
                    BART,
                    ent_1,
                    ent_2]
            rows.append(row)

        return rows

    def make_df(self, news, query):
        rows = self.make_rows_from_json(news, query)
        col_names = ['Publisher', 
                        'Title', 
                        'URL', 
                        'Image URL', 
                        'Date',
                        'Scrape',
                        'BART',
                        'NE_1',
                        'NE_2']
        df = pd.DataFrame(rows, columns=col_names)
    
        return df 
    

    # def add_column_to_df(self, df, column_name, data):
    #     df.insert(column_name, data, True)
    #     return df 

    # def prep_text_for_inference(self, df, column_name):
    #     sentances_list = [sentance for sentance in df[column_name]]
    #     return sentances_list



