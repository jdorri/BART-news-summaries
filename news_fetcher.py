import requests

import streamlit as st
from newsapi import NewsApiClient


class NewsFetcher(object):
    """
    A wrapper for extracting news for a 
    queried entity from the NewsAPI client.

    Attributes:
        query (str): user input 
        api (NewsAPIClient): the instantiated client 

    See https://github.com/mattlisiv/newsapi-python for
    further information on the Python client library.
    """

    API_KEY = '4ad210ef5a3d4c499b409f3d4fb3ab36' # place your API key here once downloaded from https://newsapi.org

    def __init__(self, query):
        self.query = query  # e.g., 'Donald Trump' 
        self.api = NewsApiClient(api_key=NewsFetcher.API_KEY)
    

    def get_everything(self):
        """
        Extracts meta-data for news articles, given
        a query passed from the user.  
        
        See https://newsapi.org/docs/endpoints/everything
        for request parameters and response fields. 

        Returns:
            news (NewsAPI): JSON response object 
        """
        from datetime import datetime
        #today = datetime.today().strftime('%Y-%m-%d')
        try:
            news = self.api.get_everything(q=self.query, # 'everything' endpoint
                                    language='en',
                                    page_size=5, # restricted due to the load of performing BART inference
                                    sort_by='relevancy') 
            return news
        except requests.exceptions.ConnectionError:
            pass
       

