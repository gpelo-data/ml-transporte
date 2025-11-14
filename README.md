# 🚀 Predictor de Duración de Viajes Urbanos

![Python](https://img.shields.io/badge/Python-blue)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-orange)
![FastAPI](https://img.shields.io/badge/FastAPI-green)
![License](https://img.shields.io/badge/License-MIT-yellow)


## 📊 Descripción
Sistema de Machine Learning para predecir la duración de viajes urbanos con **95% de precisión**.  
Proyecto completo desde EDA hasta API deployable.

## 🎯 Resultados Clave
- **R² Score**: 0.9493 📈
- **MAE**: 2.488 minutos ⏱️  
- **RMSE**: 3.089 minutos 🎯
- **Generalización**: Excelente (sin overfitting) ✅

## 🏗️ Arquitectura del Proyecto
```bash
📁 ml-transporte/  
├── 📊 notebooks/  
│ ├── 01_EDAD.ipynb # Análisis exploratorio  
│ ├── 02_FeatureEngineering.ipynb # Ingeniería de features  
│ ├── 03_Modeling.ipynb # Entrenamiento del modelo  
│ └── 04_Evaluation.ipynb # Validación y métricas  
├── 🗂️ data/  
│ ├── raw/ # Datos originales  
│ └── transformed/ # Datos procesados  
├── 🤖 models/  
│ └── modelo_duracion_viaje.pkl # Modelo serializado  
├── 🚀 api/  
│ └── main.py # API FastAPI  
```


## ⚙️ Instalación y Uso

### 1. Clonar repositorio
```bash
git clone https://github.com/gpelo-data/ml-transporte.git
cd ml-transporte
```


### 2. Instalar dependencias
```bash
    pip install -r requirements.txt
```

### 3. Ejecutar API
```bash
    cd api
    uvicorn app:app --reload
```


### 4. Probar predicción
```bash
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{
       "trip_distance_km": 3.0,
       "congestion_index": 0.3,
       "distance_congestion": 0.9,
       "rain_mm": 0.5,
       "time_block_maniana": 0,
       "time_block_tarde": 1,
       "time_block_noche": 0,
       "hour_sin": 0.5,
       "hour_cos": -0.8,
       "is_weekend": 0
     }'
```


## 🛠️ Stack Tecnológico
Lenguaje: **Python**  
ML Framework: **Scikit-learn**  
API: **FastAPI**  
Análisis: **Pandas**, **NumPy**, **Matplotlib**, **Seaborn**  
Serialización: **Joblib**  
Otros: **os**  

## 📈 Feature Engineering
🕒 Transformaciones cíclicas para variables horarias  
🔄 Variables de interacción (distancia × congestión)  
🏷️ Encoding inteligente de franjas horarias  
📅 Variables temporales (fin de semana, bloques horarios)  



## 👨‍💻 Autor
Gastón Peló - [GitHub](https://github.com/gpelo-data) - [LinkedIn](https://www.linkedin.com/in/gpelo-data/)

## 📄 Licencia
Este proyecto está bajo la Licencia MIT 

