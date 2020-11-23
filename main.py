import streamlit as st
from newsapi import NewsApiClient

from news_fetcher import NewsFetcher
from df_manager import DataFrameManager

# A news summarisation and entity-extraction tool 
# For more info on the web interface, see https://www.streamlit.io
# Author: James Dorricott  

if __name__ == "__main__":

    st.title('ABC Public Relations News App')
    query = st.text_input('Enter your client\'s name, or their company name:')

    if st.button('Get news summaries'):
        if query == '':
            st.write('Searchable query missing. Please try again.')
        else:
            news_fetcher = NewsFetcher(query)
            news = news_fetcher.get_everything() # the 'raw' news (JSON-formatted)

            df_manager = DataFrameManager()
            df = df_manager.make_df(news, query) # the reformated news (a Pandas df)

            if df.empty:
                st.write('Your search did not return any news. Please try again.')
            else:
                def display_news_element(title, image_url, body, ent_1, url, publisher):
                    """
                    In-place function for displaying multiple news tiles
                    on the Streamlit frontend. Each tile consist of:
                        - The article title
                        - The main image 
                        - A BART-generated summary
                        - The key entity in the text relative to the queried entity 
                    """
                    st.subheader(title)
                    st.image(image_url, width=200)
                    st.write('Summary: ', body)
                    if ent_1 != None:
                        st.write('Key relative entity: ', str(ent_1))
                    link = '[' + publisher + '](' + url + ')'
                    st.write('Source: ', link)
                    st.text('')

                # iterate over the above-created df  
                for i in range(len(df)):
                    title = df['Title'][i]
                    image_url = df['Image URL'][i]
                    summary = df['BART'][i][0]
                    ent_1 = df['NE_1'][i]
                    url = df['URL'][i]
                    publisher = df['Publisher'][i]
                    
                    # show the results on the frontend  
                    display_news_element(title, image_url, summary, ent_1, url, publisher)
            





    



 
  
   





