import pandas as pd


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Construye las features necesarias para el modelo.

    Args:
        df: DataFrame crudo con las columnas originales del dataset.

    Returns:
        DataFrame con nuevas columnas agregadas.
    """
    df = df.copy()

    # TODO: Crear la columna 'mental_health_score'
    # Pista: promedio de Anxiety, Depression, Insomnia y OCD
    ...

    # TODO: Crear la columna 'genre_group'
    # Pista: agrupar géneros en categorías más amplias
    # Ejemplo: {'Metal': 'heavy', 'Rock': 'heavy', 'Classical': 'clasica', ...}
    ...

    # TODO: Crear la columna 'high_listener'
    # Pista: flag binario si escucha más de 4 horas al día
    ...

    return df


GENRE_MAP: dict[str, str] = {
    # TODO: Completar con Claude Code según los géneros que aparecen en el dataset
}
