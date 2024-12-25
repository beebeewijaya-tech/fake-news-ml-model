from pydantic import BaseModel


class PredictBody(BaseModel):
    title: str
    text: str