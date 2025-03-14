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


def test_knight(df):
    """
    Creates graphs based on test_knight.csv data
    """
    plt.figure(figsize=(20, 20))
    i = 0
    for title in df.keys():
        plt.subplot(5, 6, i + 1)
        plt.hist(df[title], alpha=0.3, bins=30, color='g')
        plt.title(title)
        plt.legend(['Knight'], fontsize='small')
        i = i + 1
    plt.subplots_adjust(wspace=0.5, hspace=0.5)
    plt.show()


def train_knight(df):
    """
    Creates graphs based on train_knight.csv data
    """
    plt.figure(figsize=(20, 20))
    for i, title in enumerate(df.columns):
        if title == 'knight':
            continue
        jedidf = df[df['knight'] == 'Jedi'][title]
        sithdf = df[df['knight'] == 'Sith'][title]
        plt.subplot(5, 6, i + 1)
        plt.hist(jedidf, alpha=0.3, bins=30, color='b')
        plt.hist(sithdf, alpha=0.3, bins=30, color='r')
        plt.title(title)
        plt.legend(['Jedi', 'Sith'], fontsize='small')
    plt.subplots_adjust(wspace=0.5, hspace=0.5)
    plt.show()

def main():
    """
    Creates multiple graphs to display the effect of stats on all knights
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
        test_knight(testdf)
        train_knight(traindf)

    except Exception as e:
        print(f"Error: {str(e)}")
    return


if __name__ == "__main__":
    main()