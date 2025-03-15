import seaborn as sns
import matplotlib.pyplot as plt
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


def correlation_coefficient() -> pd.Series:
    """
    Calculates the correlation coefficient of the data in Train_knight.csv
    """
    try:
        df = load("../Train_knight.csv")
        if df is None:
            print("Error: invalid dataframe")
            return None
        df['knight'] = df['knight'].apply(lambda x: 0 if x == 'Jedi' else 1)
        correlation = df.corr()
        return correlation

    except Exception as e:
        print(f"Error: {str(e)}")
    return None


def main():
    """
    Displays a heatmap that shows the correlation coefficient between the data
    """
    corr_coeff = correlation_coefficient()
    if corr_coeff is None:
        return
    sns.heatmap(corr_coeff, annot=False)
    plt.show()
    return


if __name__ == "__main__":
    main()