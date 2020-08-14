import streamlit as st
import webbrowser

from news_fetcher import NewsFetcher
from df_manager import DataFrameManager

if __name__ == "__main__":

    st.title('ABC PR news app')

    query = st.text_input('Enter your name / company name')

    if st.button('Get news'):

        news_fetcher = NewsFetcher(query)
        news = news_fetcher.get_everything()

        df_manager = DataFrameManager()
        df = df_manager.make_df(news, query)

        def display_news_element(title, image_url, body, ent_1, ent_2):
            st.subheader(title)
            st.image(image_url, width=200)
            st.write('Summary: ', body)
            if ent_1 and ent_2 != None:
                st.write('Realtive entities: ', str(ent_1) + ', ' + str(ent_2))
            st.text('')

        for i, row in enumerate(df):
            title = df['Title'][i]
            image_url = df['Image URL'][i]
            summary = df['BART'][i][0]
            ent_1 = df['NE_1'][i]
            ent_2 = df['NE_2'][i]

            display_news_element(title, image_url, summary, ent_1, ent_2)





    



 
  
   





