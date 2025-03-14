import pandas as pd
import matplotlib.pyplot as plt


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


def main():
    """
    Prints the correlation factor between the target 'knight' and the features
    """
    try:
        df = load("../Train_knight.csv")
        if df is None:
            print("Error: invalid dataframe")
            return
        df['knight'] = df['knight'].apply(lambda x: 1 if x == 'Jedi' else 0)
        correlation = df.corr()['knight'].abs().sort_values(ascending=False)
        print(correlation)

    except Exception as e:
        print(f"Error: {str(e)}")
    return


if __name__ == "__main__":
    main()