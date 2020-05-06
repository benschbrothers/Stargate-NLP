# Stargate-NLP
first all necessary dependencies must be installed:

`pip install -r requirements.txt`

## Preprocessing
For this purpose the database is crawled with the scrapper into an HTML folder and prepared for further processing as far as possible:
`python scrapper.py`

## NLP
Then the POS tagging script can be started, which accesses the scraped HTML data
`python run.py`