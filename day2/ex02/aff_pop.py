from load_csv import load
import matplotlib.pyplot as plt


def convert_kMB(val) -> float:
    """This function converts data that ends with k, M, B"""
    if isinstance(val, str) and val.endswith('k'):
        return float(val[:-1]) * 1000
    elif isinstance(val, str) and val.endswith('M'):
        return float(val[:-1]) * 1000000
    elif isinstance(val, str) and val.endswith('B'):
        return float(val[:-1]) * 1000000000
    return float(val)


def correctdisplay(val) -> str:
    """This function converts data that ends with k, M, B"""
    if isinstance(val, (int, float)) and val > 1000000000:
        return f"{int(val / 1000000000)}B"
    elif isinstance(val, (int, float)) and val > 1000000:
        return f"{int(val / 1000000)}M"
    elif isinstance(val, (int, float)) and val > 1000:
        return f"{int(val / 1000)}k"
    return f"{int(val)}"


def main():
    """
    This program calls the load function,
    loads the file population_total.csv,
    and displays the country information versus other
    country of your choice.
    """
    try:
        df = load("population_total.csv")
        if df is None:
            print("Error: invalid dataframe")
            return
        if not any(item == "country" for item in df.columns):
            print("Error: no column is named 'country'")
            return

        country = "France"
        other = "Belgium"
        df = df.set_index("country")
        newdf = df.loc[country]
        otherdf = df.loc[other]
        newdf = newdf["1800":"2050"]
        otherdf = otherdf["1800":"2050"]
        newdf = newdf.apply(convert_kMB)
        otherdf = otherdf.apply(convert_kMB)
        max_val = max(max(newdf.values), max(otherdf.values))
        ticks = [max_val * 0.9, max_val * 0.6, max_val * 0.3]

        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.title("Population Projections")
        plt.plot(newdf.index, newdf.values, label=country, color='g')
        plt.plot(otherdf.index, otherdf.values, label=other, color='b')
        plt.xticks(newdf.index[::40])
        plt.yticks(ticks, [correctdisplay(item) for item in ticks])
        plt.legend(loc="lower right")
        plt.show()
    except Exception as e:
        print(f"Error: {str(e)}")
        return
    return


if __name__ == "__main__":
    main()
