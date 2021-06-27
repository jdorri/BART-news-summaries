# RBCxImperial News Summarisation App

This is a prototype of a data science tool to help Public Relations professionals keep track of the potential mass of news content on their clients and react timely. The work was completed during the interview stages of a PhD with Imperial's Data Science Institute and Royal Bank of Canada and makes use of a modern NLP stack of Transformers, spaCy, and Streamlit. 

## Installation

The application is based in Python 3.7 and requires the following packages:

* pandas 
* streamlit
* newsapi
* transformers 
* torch 
* spacy
* newspaper

These dependencies can be installed with (after first sourcing into a newly-created virtual environment):

```
pip install -r requirements.txt
```

The next stage is to create an API key for [News API](https://newsapi.org), ours news aggregator. Once a key has been downloaded, place it in ```news_fetcher.py```.

Note: spaCy's ```en_core_web_sm``` model is installed with the requirements file rather than at the command line.

## Usage

The application uses [Streamlit](https://www.streamlit.io) for displaying news items on an interactive web page. 

To run the application, move to the top level of this directory and run the following command:

```
streamlit run main.py
```

This will open a new page on your default browser, using localhost as host. 

At the top is a text box for entering a search query, e.g., 'Donald Trump'. After that, press the 'Get news' button below it and live news will be displayed (for the current day), consisting of the article title, an image thumbnail, an AI-generated summary, and key entities relative to the queried entity. 

NOTE: To generate the news summaries, we use BART (BART-large-CNN), a pre-trained language model with SOTA summarisation capabilities. The first time the code is run, BART will automatically be downloaded. This may take some time (model size: 1.6GB).

## Warning

For this prototype, we use a CPU to perform BART inference. Because of the size of the model, we recommend using a strong CPU if you want to scale up the amount of news processed. 

Also, Transformers will raise a warning about using the model without further fine tuning - this is fine to ignore. 

## Screenshot

Here is a screenshot of the tool:

![The Sreamlit news app](screenshots/screenshot.png)
