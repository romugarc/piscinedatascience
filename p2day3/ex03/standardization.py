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


def scatter_1(testdf, traindf):
    """
    Creates scatter plot that correlates Empowered and Stims features for knights
    """
    plt.xlabel("Empowered")
    plt.ylabel("Stims")
    plt.scatter(testdf['Empowered'], testdf['Stims'], alpha=0.3, color='g')
    plt.legend(["Knight"],loc='upper left')
    plt.show()

    jedi_empowered = traindf[traindf['knight'] == 'Jedi']['Empowered']
    jedi_stims = traindf[traindf['knight'] == 'Jedi']['Stims']
    sith_empowered = traindf[traindf['knight'] == 'Sith']['Empowered']
    sith_stims = traindf[traindf['knight'] == 'Sith']['Stims']
    plt.xlabel("Empowered")
    plt.ylabel("Stims")
    plt.scatter(jedi_empowered, jedi_stims, alpha=0.3, color='b')
    plt.scatter(sith_empowered, sith_stims, alpha=0.3, color='r')
    plt.legend(["Jedi", "Sith"],loc='upper left')
    plt.show()


def main():
    """
    Prints the standardized version of the data and shows an example scatter plot based on this standardized data
    """
    try:
        testdf = load("../Test_knight.csv")
        if testdf is None:
            print("Error: invalid dataframe")
            return
        traindf = load("../Train_knight.csv")
        if traindf is None:
            print("Error: invalid dataframe")
            return
        print(testdf)
        for column in testdf.columns:
            if column == 'knight':
                continue
            testdf[column] = (testdf[column] - testdf[column].mean()) / testdf[column].std()
        for column in traindf.columns:
            if column == 'knight':
                continue
            traindf[column] = (traindf[column] - traindf[column].mean()) / traindf[column].std()
        print(testdf)
        scatter_1(testdf, traindf)

    except Exception as e:
        print(f"Error: {str(e)}")
    return


if __name__ == "__main__":
    main()