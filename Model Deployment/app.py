from fastapi import FastAPI
from pydantic import BaseModel
import joblib

## Load model
model = joblib.load("model.joblib")

# order of the features the model needs
FEATURE_NAMES = [
    "MedInc",
    "HouseAge",
    "AveRooms",
    "AveBedrms",
    "Population",
    "AveOccup",
    "Latitude",
    "Longitude",
]

## Create FastAPI app
app = FastAPI(
    title="House Price Prediction API",
    description="Predict California house price using a trained ML model",
    version="1.0"
)


## Request schema
class HouseFeatures(BaseModel):
    features: list[float]


@app.get("/")
def home():
    return {
        "message": "Welcome to the House Price Prediction API!",
        "docs": "/docs"
    }


@app.get("/health")
def health():
    return {"status": "ok"}
