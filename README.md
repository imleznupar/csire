# CSIRE

A project that aims to enhance the rapid earthquake response by analyzing casualty information collected from social media.

## Requirements

The following libraries are required:
* numpy
* pandas
* word2number
* nltk
* language_tool_python
* folium
* [morcedai](https://github.com/openeventdata/mordecai#installation-and-requirements)
* spacy
* wordsegment
* keras


## Usage

1. clone repository
2. run the follwing code

```python
python runner.py "input_path" "country_code"
```
3. The file 'map.html' will be generated, which is an interactive map of the casualty information. Also, 'processed.csv' can give more detailed information of the map.

## Example
Using 'example.csv' input file, the program should out the map below:
 

## How it works
#### Preprocess 
Tweets collected during earthquakes undergo the process of removing emoji, URL, mentions and applying word segmentation, spelling correction. 
#### Filter Irrelevant Information
Deep learning models trained to identify earthquake and casualty information. Default model is LSTM (best performance in testing), other models available: RNN, GRU, Bi-Directional LSTM, Bi-Directional LSTM with Attention (see models folder). Trained on [HumanAID dataset](https://crisisnlp.qcri.org/humaid_dataset).
#### Extract Casualty Information 
A custom named entity recognizer trained with [StanfordNERTagger](https://nlp.stanford.edu/software/crf-faq.shtml#b) is used to identify death, injury, and missing numbers. Then, numbers are parsed to convert string of number to integers.
#### Extract Geological Information 
[Morcedai](https://github.com/openeventdata/mordecai), a python library for full text geoparsing. Only tweets that contain location in the country specified are kept.
#### Generate Map
Uses folium to generate an interactive map with locations labeled with location name, number of deaths, injures, and missings.


## Acknowledgements

The geoparser used in this project is [morcedai](https://github.com/openeventdata/mordecai).

For further inquiries, please contact jasminelu23@gmail.com
