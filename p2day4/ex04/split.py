import sys
import pandas as pd
import matplotlib.pyplot as plt


def load(path: str) -> pd.DataFrame:
    """
    This function takes a path as argument,
    writes the dimensions of the data set and returns it.
    """
    if not isinstance(path, str):
        return None
    if path is None:
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
    Prints the normalized version of the data and shows an example scatter plot based on this normalized data
    """
    if len(sys.argv) != 2:
        print("Error: Need a single argument")
        return
    try:
        df = load(f"{sys.argv[1]}")
        if df is None:
            print("Error: invalid dataframe")
            return
        newdf = df.sample(frac = 0.75)
        restdf = df.drop(newdf.index)

        newdf.to_csv("Training_knight.csv", index=False, header=True)
        restdf.to_csv("Validation.csv", index=False, header=True)

    except Exception as e:
        print(f"Error: {str(e)}")
    return


if __name__ == "__main__":
    main()