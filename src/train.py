import os
import joblib
import pandas as pd
from dotenv import load_dotenv
from sklearn.model_selection import train_test_split

from features import build_features

load_dotenv()

DATA_PATH = os.getenv("TRAIN_DATA_PATH", "data/train.csv")
MODEL_PATH = os.getenv("MODEL_PATH", "model/pipeline.joblib")
TARGET = "Music effects"


def load_data(path: str) -> pd.DataFrame:
    """Carga el dataset desde un CSV."""
    # TODO: Cargar el CSV y retornar un DataFrame
    ...


def split_features_target(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    """Separa features y variable objetivo."""
    # TODO: Separar X e y, donde y es la columna TARGET
    ...


def build_pipeline():
    """
    Construye el Pipeline de scikit-learn con preprocesamiento y clasificador.

    Returns:
        Pipeline sin entrenar.
    """
    # TODO: Con Claude Code, armar el pipeline completo:
    # - ColumnTransformer para variables numéricas (StandardScaler)
    #   y categóricas (OneHotEncoder)
    # - RandomForestClassifier como modelo final
    ...


def train(data_path: str = DATA_PATH, model_path: str = MODEL_PATH) -> None:
    """Ejecuta el flujo completo de entrenamiento y guarda el modelo."""
    df = load_data(data_path)
    df = build_features(df)

    X, y = split_features_target(df)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    pipeline = build_pipeline()

    # TODO: Entrenar el pipeline
    ...

    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(pipeline, model_path)
    print(f"Modelo guardado en {model_path}")

    return X_test, y_test, pipeline


if __name__ == "__main__":
    train()
