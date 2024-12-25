import pickle
import pandas as pd
from pathlib import Path

from src.schema.predict import PredictBody

def predicting(body: PredictBody):
  path = Path("src/models")


  with open(f'{path}/fake-news.pkl', 'rb') as f:
    mod = pickle.load(f)

  with open(f'{path}/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

  try:
    inp = pd.Series([body.text])
    inp = vectorizer.transform(inp)

    res = int(mod.predict(inp)[0])
    return {
      "message": "Successful predicting",
      "res": res == 1
    }
  except Exception as e:
    raise e