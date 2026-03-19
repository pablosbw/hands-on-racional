import pandas as pd
from sklearn.pipeline import Pipeline


def classification_report_df(pipeline: Pipeline, X_test: pd.DataFrame, y_test: pd.Series) -> str:
    """
    Genera el reporte de clasificación.

    Args:
        pipeline: Pipeline entrenado.
        X_test: Features de test.
        y_test: Etiquetas reales.

    Returns:
        Reporte como string.
    """
    # TODO: Generar y retornar el classification_report de sklearn
    ...


def plot_confusion_matrix(pipeline: Pipeline, X_test: pd.DataFrame, y_test: pd.Series) -> None:
    """
    Genera y muestra la matriz de confusión.

    Args:
        pipeline: Pipeline entrenado.
        X_test: Features de test.
        y_test: Etiquetas reales.
    """
    # TODO: Con Claude Code, graficar la matriz de confusión con seaborn
    ...


def feature_importance(pipeline: Pipeline, feature_names: list[str]) -> pd.DataFrame:
    """
    Extrae la importancia de features del modelo.

    Args:
        pipeline: Pipeline entrenado (debe contener un RandomForestClassifier).
        feature_names: Nombres de las features después del preprocesamiento.

    Returns:
        DataFrame con columnas ['feature', 'importance'] ordenado descendente.
    """
    # TODO: Extraer feature importances del clasificador dentro del pipeline
    ...
