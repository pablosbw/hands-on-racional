import os
import csv
import datetime
import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

MODEL_PATH = os.getenv("MODEL_PATH", "model/pipeline.joblib")
LOG_PATH = os.getenv("LOG_PATH", "logs/predictions.csv")

app = FastAPI(title="Music & Mental Health Classifier")

# TODO: Cargar el pipeline entrenado al iniciar la app
pipeline = None  # pipeline = joblib.load(MODEL_PATH)


class InputData(BaseModel):
    Age: int
    Hours_per_day: float
    Fav_genre: str
    Anxiety: int
    Depression: int
    Insomnia: int
    OCD: int


def log_prediction(input_data: dict, prediction: str) -> None:
    """Registra cada predicción en un CSV de logs."""
    # TODO: Con Claude Code, implementar el logging a LOG_PATH
    # Incluir timestamp, todos los campos de entrada y la predicción
    ...


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(data: InputData):
    """
    Recibe datos de un usuario y retorna la predicción del modelo.

    Returns:
        {"prediction": "Improve" | "No effect" | "Worsen"}
    """
    # TODO: Con Claude Code, completar este endpoint:
    # 1. Convertir InputData a DataFrame (renombrar campos si es necesario)
    # 2. Llamar a build_features para agregar las features engineered
    # 3. Predecir con el pipeline
    # 4. Llamar a log_prediction para registrar el resultado
    # 5. Retornar la predicción
    ...
