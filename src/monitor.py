import pandas as pd


def check_drift(log_path: str, train_path: str, column: str, threshold: float = 0.2) -> dict:
    """
    Alerta si la media de una columna numérica se desvía más de `threshold`
    respecto a los datos de entrenamiento.

    Args:
        log_path:   Ruta al CSV de predicciones logueadas.
        train_path: Ruta al CSV de entrenamiento.
        column:     Nombre de la columna a comparar.
        threshold:  Diferencia absoluta máxima permitida entre medias.

    Returns:
        Dict con 'train_mean', 'current_mean', 'drift' (float) y 'alert' (bool).
    """
    # TODO: Con Claude Code, implementar la comparación de distribuciones
    ...


def prediction_distribution(log_path: str) -> pd.Series:
    """
    Retorna la distribución de predicciones registradas en el log.

    Args:
        log_path: Ruta al CSV de predicciones.

    Returns:
        Series con conteo de cada clase predicha.
    """
    # TODO: Leer el log y contar las ocurrencias de cada predicción
    ...
