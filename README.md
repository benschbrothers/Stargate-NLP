# Stargate-NLP
first all necessary dependencies must be installed:

`pip install -r requirements.txt`

## Preprocessing
For this purpose the database is crawled into an HTML folder and cropped for further processing as far as possible:
`python crawler.py`

## NLP
Then the POS tagging script can be started, which accesses the cropped HTML data
`python pos-tagging.py`

Some Named Entity Recogition (NER) tests are done with
`python entity-extraction.py`