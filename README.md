# Let's Code with Claude — Taller de Data Science

**Duración:** 2h 15min | **Nivel:** Intermedio | **Herramienta:** Claude Code

Clasificador de efectos de la música en la salud mental usando el dataset
[Music & Mental Health Survey](https://www.kaggle.com/datasets/catherinerasgaitis/mxmh-survey-results).

---

## Setup

```bash
# 1. Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Copiar variables de entorno
cp .env.example .env
```

> **Dataset:** Descarga `mxmh_survey_results.csv` desde Kaggle y reemplaza `data/train.csv`.

---

## Estructura

```
lets-code-with-claude/
├── data/
│   ├── train.csv           ← dataset de entrenamiento
│   └── test_data.csv       ← mini CSV para probar el endpoint
├── notebooks/
│   └── 01_eda.ipynb        ← EDA con TODOs estratégicos (Bloque 1)
├── src/
│   ├── features.py         ← feature engineering (Bloque 1 & 2)
│   ├── train.py            ← entrenamiento + pipeline (Bloque 2 & 3)
│   ├── evaluate.py         ← métricas y visualizaciones (Bloque 2)
│   └── monitor.py          ← detección de drift (Bloque 5)
├── model/                  ← artefactos serializados (.joblib)
├── logs/                   ← predicciones registradas (.csv)
├── app.py                  ← API FastAPI (Bloque 4)
├── consume_endpoint.py     ← cliente del endpoint (Bloque 4)
├── requirements.txt
└── .env.example
```

---

## Flujo del taller

```
Bloque 1  →  notebooks/01_eda.ipynb       EDA + Feature Engineering
Bloque 2  →  src/features.py / train.py   Notebook → módulos Python
Bloque 3  →  src/train.py                 Pipeline sklearn serializable
Bloque 4  →  app.py                       Deploy local con FastAPI
Bloque 5  →  src/monitor.py               Logging + detección de drift
```

---

## Comandos útiles

```bash
# Entrenar el modelo
python src/train.py

# Levantar la API
uvicorn app:app --reload

# Consumir el endpoint con el CSV de prueba
python consume_endpoint.py

# Docs interactivas de la API
open http://localhost:8000/docs
```
