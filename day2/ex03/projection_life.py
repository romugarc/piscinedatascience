from load_csv import load
import matplotlib.pyplot as plt
import numpy as np


def main():
    """
    This program calls the load function,
    loads the files
    'income_per_person_gdppercapita__ppp_inflation_adjusted.csv'
    and 'life_expectancy_years.csv',
    and displays the projection of life expectancy in relation to the
    gross national product of the year 1900 for each country
    """
    inc_df = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_df = load("life_expectancy_years.csv")
    if inc_df is None or life_df is None:
        print("Error: invalid dataframe")
        return

    year = "1900"
    inc_df = inc_df[year]
    life_df = life_df[year]
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life expectancy")
    plt.title(year)
    plt.scatter(inc_df.values, life_df.values)
    plt.xscale("log")
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
    plt.yticks(np.arange(20, 56, 5))
    plt.show()
    return


if __name__ == "__main__":
    main()
