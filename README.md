## Project Introduction
This project focuses on developing a classification model for identifying fake news

1. Our primary goal is to achieve high accuracy in classifying news articles as true or false.
2. The model will be trained, validated, and tested using this curated dataset, aiming for a robust solution in fake news detection.

![project](./docs/predict.gif)

## How to run

```bash
  python3 -m venv venv

  source venv/bin/activate

  pip3 install -r requirements.txt
  
  fastapi dev main.py
```

## CURL

Successful case
``` bash
curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "After 20 years, the post-tsunami generation stays vigilant for future disasters",
  "text": "On Dec. 26, 2004, a powerful 9.1-magnitude earthquake, off the coast of the Indonesian island of Sumatra, triggered a tsunami that killed around 230,000 people across a dozen countries, reaching as far as East Africa. Some 160,000 of those were in Aceh, at the northwestern tip of Indonesia."
}'

----

Response Body
{
  "message": "Successful predicting",
  "res": true
}
```


Failed case
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "Draft Senate Iran legislation sets tough new U.S. terms for deal",
  "text": "A cow eating a snake with a little bit of problem when US terms is not good"
}'

-----
	
Response body
{
  "message": "Successful predicting",
  "res": false
}
```



## Methodology

1. Data Cleaning and EDA (Exploratory Data Analysis)

2. Data Cleaning: We meticulously clean the dataset to handle missing values, remove duplicates, and correct inconsistencies, ensuring the quality of our input data.
Exploratory Data Analysis (EDA): Through EDA, we analyze the dataset's structure, content, and distribution to gain insights into the data characteristics, identify patterns, and uncover any underlying issues that could affect model performance.


## Kaggle

### [Data Source](https://www.kaggle.com/datasets/aadyasingh55/fake-news-classification)

The dataset provides a binary classification of news articles, making it an essential resource for those researching or developing solutions in the field of misinformation and fake news detection. This is the initial version of the dataset, focused on enhancing the capabilities of Transformer models in identifying fake news.
