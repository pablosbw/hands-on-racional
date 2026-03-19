"""
Script para consumir el endpoint /predict con los registros de test_data.csv.
Ejecutar con el servidor levantado: uvicorn app:app --reload
"""
import pandas as pd
import requests

BASE_URL = "http://localhost:8000"
TEST_DATA_PATH = "data/test_data.csv"


def main() -> None:
    df = pd.read_csv(TEST_DATA_PATH)

    # TODO: Con Claude Code, iterar las filas y enviar cada una al endpoint
    # Renombrar la columna 'Hours per day' → 'Hours_per_day' y
    # 'Fav genre' → 'Fav_genre' para que coincida con el schema de la API
    for _, row in df.iterrows():
        ...


if __name__ == "__main__":
    main()
