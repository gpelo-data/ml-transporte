# -------------
# 📚 Librerías
# -------------

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd


# ------------------
# 🏁 Inicialización
# ------------------

app = FastAPI(
    title = 'Modelo de Predicción de Duración de Viajes',
    description = 'API para predecir la duración de los viajes usando regresión lineal',
    version = '1.0'
)

# Cargamos el modelo
pipeline = joblib.load('../models/modelo_duracion_viaje.pkl')


# -------------------------
# 📝 Definición del Schema
# -------------------------

class TravelFeatures(BaseModel):
    trip_distance_km : float
    congestion_index: float
    distance_congestion: float
    rain_mm: float
    time_maniana: int
    time_tarde: int
    time_noche: int
    hour_sin: float
    hour_cos: float
    is_weekend: int


# --------------
# 🔴 Endpoints
# --------------

@app.get('/health')
def health_check():
    return {'status' : 'ok'}

@app.get("/model/metrics")
def model_metrics():
    return {
        "r2_score": 0.9493,
        "mae": 2.488,
        "rmse": 3.089,
        "performance": "Excelente"
    }
    

@app.get("/model/info")
def model_info():
    return {
        "model": "Regresión Lineal",
        "version": "1.0",
        "features": [
            "trip_distance_km",
            "congestion_index",
            "distance_congestion",
            "rain_mm",
            "time_maniana",
            "time_tarde",
            "time_noche",
            "hour_sin",
            "hour_cos",
            "is_weekend"
        ]
    }


@app.post("/predict")
def predict(features: TravelFeatures):

    # ✅ Convertir entrada en DataFrame con nombres de columnas
    df = pd.DataFrame([features.dict()])

    # ✅ Predecir
    prediction = pipeline.predict(df)[0]

    return {
        "prediccion_minutos": float(prediction),
        "detalle": "Duración estimada del viaje en minutos"
    }


@app.get("/predict/example")
def predict_example():
    """Endpoint de ejemplo con valores típicos"""
    example_data = {
        "trip_distance_km": 3.0,
        "congestion_index": 0.3,
        "distance_congestion": 0.9,
        "rain_mm": 0.5,
        "time_maniana": 0,
        "time_tarde": 1,
        "time_noche": 0,
        "hour_sin": 0.5,
        "hour_cos": -0.8,
        "is_weekend": 0
    }
    
    df = pd.DataFrame([example_data])
    prediction = pipeline.predict(df)[0]
    
    return {
        "ejemplo": example_data,
        "prediccion_minutos": round(float(prediction), 2)
    }


