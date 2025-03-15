import pandas as pd
from sklearn import decomposition, preprocessing
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

        pca_data = preprocessing.scale(df)

        pca = decomposition.PCA(n_components=len(df.columns))
        pca.fit(pca_data)
        cum_var = []
        for i in range(0, len(pca.explained_variance_ratio_)):
            if i == 0:
                cum_var.append(pca.explained_variance_ratio_[i])
            else:
                cum_var.append(pca.explained_variance_ratio_[i] + cum_var[i-1])
        toplot = [float(item * 100) for item in cum_var]
        
        print("Variances (Percentage):")
        print(pca.explained_variance_ratio_, "\n")
        print("Cumulative Variances (Percentage):")
        print(toplot)
        print("Components needed to reach 90 percent cumulative variance:")
        print([item for item in toplot if item < 91])
        
        plt.xlabel("Number of components")
        plt.ylabel("Explained variance (%)")
        plt.plot(toplot)
        plt.show()


    except Exception as e:
        print(f"{str(e)}")
    return


if __name__ == "__main__":
    main()