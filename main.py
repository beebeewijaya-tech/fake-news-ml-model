from typing import Union

from fastapi import FastAPI

from src.services import predict as predict_service
from src.schema import predict as predict_schema

app = FastAPI()


@app.post("/predict")
def model_predict(body: predict_schema.PredictBody):
    return predict_service.predicting(body)