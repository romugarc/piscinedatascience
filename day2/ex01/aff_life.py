from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    This program calls the load function,
    loads the file life_expectancy_years.csv,
    and displays the country information
    """
    df = load("life_expectancy_years.csv")
    if df is None:
        print("Error: invalid dataframe")
        return
    if not any(item == "country" for item in df.columns):
        print("Error: no column is named 'country'")
        return
    country = "France"
    df = df.set_index("country")
    newdf = df.loc[country]
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.title(f"{country} Life expectancy Projections")
    plt.plot(newdf.index, newdf.values)
    plt.xticks(newdf.index[::40])
    plt.show()
    return


if __name__ == "__main__":
    main()
