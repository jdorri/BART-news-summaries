# ABC Public Relations News App

This is a prototype of a news summarisation and entity-extraction tool for a hypothetical public relations firm, ABC Public Relations. With this app, public relations professionals can keep track of the potential mass of news content on their clients and react timely. 

## Installation

The application is based in Python 3.7 and requires the following packages:

* pandas 
* streamlit
* newsapi
* transformers 
* spacy
* newspaper

These dependencies can be installed with (after first sourcing into a newly-created virtual environment):

```
pip install -r requirements.txt
```

The next stage is to create an API key for [News API](https://newsapi.org), ours news aggregator. Once a key has been downloaded, place it in ```news_fetcher.py```.

Note: SpaCy's ```en_core_web_sm``` model is installed with the requirements file rather than at the command line.

## Usage

The application uses [Streamlit](https://www.streamlit.io) for displaying news items on an interactive web page. 

To run the application, move to the top level of this directory and run the following command:

```
streamlit run main.py
```

This will open a new page on your default browser, using localhost as host. 

At the top is a text box for entering a search query, e.g., 'Nicola Sturgeon'. After that, press the 'Get news' button below it and live news will be displayed (for the current day), consisting of the article title, an image thumbnail, a summary of the article, and key entities relative to the queried entity. 

NOTE: To generate the article summaries, we use BART (BART-large-CNN), a pre-trained language model with summarisation capabilities. The first time the code is run, BART will automatically be downloaded. This may take some time (size: 1.6GB). 

## Warning

It is possible to use BART for inference on a CPU. However, because of the size of the BART model, we recommend using a good CPU when using this prototype. 

Also, Transformers will raise a warning about using the model without further fine tuning - this is fine to ignore. 

## Contributions 

This app was built in a matter of a few days, showing the power of modern APIs such as Hugging Face and streamlit. If you have an idea of how you'd like to improve it, feel free to contribute your changes.

## Screenshot

Here is a screenshot:

![The Sreamlit news app](screenshots/screenshot.png)
