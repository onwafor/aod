from fastapi import FastAPI
from pydantic import BaseModel
from model_utils import predict_all

app = FastAPI()

class InputData(BaseModel):
    actual_irr: float
    clear_sky_irr: float
    month: int
    temp: float
    pressure: float
    dew_point: float
    wind: float
    humidity: float
    aod_lag1: float
    aod_lag2: float
    aod_roll3: float

@app.post("/predict")
def predict(data: InputData):
    return predict_all(data)