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


## Methodology

1. Data Cleaning and EDA (Exploratory Data Analysis)

2. Data Cleaning: We meticulously clean the dataset to handle missing values, remove duplicates, and correct inconsistencies, ensuring the quality of our input data.
Exploratory Data Analysis (EDA): Through EDA, we analyze the dataset's structure, content, and distribution to gain insights into the data characteristics, identify patterns, and uncover any underlying issues that could affect model performance.


## Kaggle

### [Data Source](https://www.kaggle.com/datasets/aadyasingh55/fake-news-classification)

The dataset provides a binary classification of news articles, making it an essential resource for those researching or developing solutions in the field of misinformation and fake news detection. This is the initial version of the dataset, focused on enhancing the capabilities of Transformer models in identifying fake news.
