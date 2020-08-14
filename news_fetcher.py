import requests

from newsapi import NewsApiClient

class NewsFetcher(object):

    API_KEY = '4ad210ef5a3d4c499b409f3d4fb3ab36' # place your API key here

    def __init__(self, query):
        self.query = query  
        self.api = NewsApiClient(api_key=NewsFetcher.API_KEY)
    
    def get_everything(self):
        from datetime import datetime
        today = datetime.today().strftime('%Y-%m-%d')
        try:
            news = self.api.get_everything(q=self.query,
                                    language='en',
                                    from_param=today)
            return news
        except requests.exceptions.ConnectionError:
            pass

