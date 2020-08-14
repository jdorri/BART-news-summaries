from transformers import pipeline 
import pandas as pd 
import streamlit as st
from newsapi import NewsApiClient


# st.title('ABC news app')
# query = st.text_input('Identify yourself (name/company)')

def get_news_from_NEWSAPI(query):
    try:
        API_KEY = '4ad210ef5a3d4c499b409f3d4fb3ab36'
        api = NewsApiClient(api_key=API_KEY)
        news = api.get_everything(q=query,
                                language='en',
                                from_param='2020-08-10')
        return news
    except requests.exceptions.ConnectionError:
        print('Failed to download news')
    
# def extract_urls_from_json(json):
#     urls = []
#     for article in json['articles']:
#         url = article['url'] 
#         urls.append(url)
#     return urls 

def create_df_from_news(news):
    rows = []
    for article in news['articles']:
        identifier = article['source']['id']
        publisher = article['source']['name']
        author = article['author']
        title = article['title']
        description = article['description']
        url = article['url']
        image_url = article['urlToImage']
        date = article['publishedAt']
        content = article['content']
        row = [identifier, 
                    publisher, 
                    author, title, 
                    description, 
                    url, 
                    image_url, 
                    date, 
                    content]
        rows.append(row)
        
    #df = pd.DataFrame.from_records(rows)
    columns = ["ID", 
                    "Publisher", 
                    "Author", 
                    "Title", 
                    "Description",
                    "URL", 
                    "Image URL",
                    "Date",
                    "Content"]
    df = pd.DataFrame(rows, columns=columns)
    return df

def get_pipeline_from_transformers(task):
    pipeline = pipeline(task)
    return pipeline 

def make_inference(text, pipeline):
    results = pipeline(text)
    return results

def prepare_text_for_inference(df, column_name):
    list_of_sentances = [title for title in df[column_name]]
    return list_of_sentances

def add_column_to_df(df, column_name, data):
    df.insert(column_name, data, True)
    return df

if __name__ == "__main__":
    query = 'Trump'
    news = get_news_from_NEWSAPI(query)
    df = create_df_from_news(news)

    print(df.head())

    # for text in df['Title']:
    #     print('Testing classifier on the following text: ', text)

    # sentiment = get_sentiment(text)
    # print('The predicted sentiment is: ', sentiment)

    # sentances = prepare_text_for_classification(df)
    # results = get_sentiment(sentances)
        
    # for i, result in enumerate(results):
    #     print(sentances[i])
    #     print(f"label: {result['label']}, with score: {round(result['score'], 4)}")
    #     print()

  






                                    
