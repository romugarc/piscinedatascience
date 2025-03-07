import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    This function takes a path as argument,
    writes the dimensions of the data set and returns it.
    """
    if not isinstance(path, str):
        return None
    try:
        df = pd.read_csv(path)
        print("Loading dataset of dimensions", df.shape)
        return df
    except Exception as e:
        print(f"Error:{str(e)}")
        return None
