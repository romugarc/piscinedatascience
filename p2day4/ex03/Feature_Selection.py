import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor


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


def standardization(df):
    for column in df.columns:
        df[column] = (df[column] - df[column].mean()) / df[column].std()


def main():
    """
    Displays a heatmap that shows the correlation coefficient between the data
    """
    try:
        df = load("../Train_knight.csv")
        if df is None:
            print("Error: invalid dataframe")
            return None
        df['knight'] = df['knight'].apply(lambda x: 0 if x == 'Jedi' else 1)
        standardization(df)
        
        vif = pd.DataFrame()
        vif.index = df.columns
        vif["VIF"] = [variance_inflation_factor(df.values, i) for i in range(len(df.columns))]
        vif["Tolerance"] = [1 / item for item in vif["VIF"]]
        print(vif)
        
        clean_data = vif[vif["VIF"] < 5]
        print(clean_data)


    except Exception as e:
        print(f"{str(e)}")
    return


if __name__ == "__main__":
    main()