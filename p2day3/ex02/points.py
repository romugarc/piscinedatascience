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


def scatter_2(testdf, traindf):
    """
    Creates scatter plot that correlates Push and Deflection features for knights
    """
    plt.xlabel("Push")
    plt.ylabel("Deflection")
    plt.scatter(testdf['Push'], testdf['Deflection'], alpha=0.3, color='g')
    plt.legend(["Knight"],loc='upper left')
    plt.show()

    jedi_push = traindf[traindf['knight'] == 'Jedi']['Push']
    jedi_deflection = traindf[traindf['knight'] == 'Jedi']['Deflection']
    sith_push = traindf[traindf['knight'] == 'Sith']['Push']
    sith_deflection = traindf[traindf['knight'] == 'Sith']['Deflection']
    plt.xlabel("Push")
    plt.ylabel("Deflection")
    plt.scatter(jedi_push, jedi_deflection, alpha=0.3, color='b')
    plt.scatter(sith_push, sith_deflection, alpha=0.3, color='r')
    plt.legend(["Jedi", "Sith"],loc='upper left')
    plt.show()


def main():
    """
    Prints several scatter plots
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
        scatter_1(testdf, traindf)
        scatter_2(testdf, traindf)

    except Exception as e:
        print(f"Error: {str(e)}")
    return


if __name__ == "__main__":
    main()