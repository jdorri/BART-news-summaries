# RBCxImperial News Summarisation App

This is a prototype of a data science tool to help Public Relations professionals keep track of the potential mass of news content on their clients and react timely. The work was completed during the interview stages of a PhD with Imperial's Data Science Institute and makes use of a modern NLP stack of Transformers, spaCy, and Streamlit. 

## Setup

The app is based on Python 3.7 and requires the following packages:

* pandas 
* streamlit
* newsapi
* transformers 
* torch 
* spacy
* newspaper

After sourcing into a newly-created virtual environment, these can be installed with:

```
pip install -r requirements.txt
```

Then, create an API key for [News API](https://newsapi.org), ours news aggregator. Once downloaded, place it in ```news_fetcher.py```.

Note: spaCy's ```en_core_web_sm``` model is installed with the requirements file rather than at the command line.

## Usage

The application uses [Streamlit](https://www.streamlit.io) for displaying news items on an interactive web page. 

To use the app, from the top level of this directory, simply run:

```
streamlit run main.py
```

This will open a new page on your default browser, using localhost as host. 

At the top is a text box for entering a search query. After that, press the 'Get news' button below it and live news will be displayed, consisting of the article title, an image thumbnail, a summary, and key entities relative to the queried entity. 

To generate the news summaries, I use [BART](https://arxiv.org/pdf/1910.13461.pdf) (BART-large-CNN), a pre-trained language model with SOTA summarisation capabilities. The first time the app is run, BART will be automatically downloaded and cached locally. 

## CPU support only 

Because of the large model size (1.6GB), consider using a GPU if you want to scale up the amount of news processed. Also, Transformers will also raise a warning about using the model without fine tuning - this is fine to ignore.

## Screenshot

Here is a screenshot of the tool:

![The Sreamlit news app](screenshots/screenshot.png)
