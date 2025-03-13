import psycopg2
import os
from dotenv import load_dotenv
from matplotlib import pyplot as plt

def get_data():
    connection_params = {
        'dbname': os.getenv("POSTGRES_DB"),
        'user': os.getenv("POSTGRES_USER"),
        'password': os.getenv("POSTGRES_PASSWORD"),
        'host': os.getenv("HOST"),
        'port': os.getenv("POSTGRES_PORT")
    }

    connection = psycopg2.connect(**connection_params)
    cursor = connection.cursor()
    result = []
    result1 = []
    result2 = []
    try:

        sql_query = """SELECT 
        COUNT(price) AS count,
        AVG(price) AS mean,
        STDDEV(price) AS std,
        MIN(price) AS min,
        PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY price) AS "25%",
        PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY price) AS "50%",
        PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY price) AS "75%",
        MAX(price) AS max
        FROM customers
        WHERE event_type = 'purchase'
        AND event_time BETWEEN '2022-10-01 00:00:00' AND '2023-02-28 23:59:59';
        """
        cursor.execute(sql_query)
        result = cursor.fetchall()

        sql_query = """SELECT price
        FROM customers
        WHERE event_type = 'purchase'
        AND event_time BETWEEN '2022-10-01 00:00:00' AND '2023-02-28 23:59:59';
        """
        cursor.execute(sql_query)
        result1 = cursor.fetchall()

        sql_query = """SELECT user_id, AVG(price) AS average_basket_price
                        FROM customers
                        WHERE event_type = 'cart'
                        AND event_time BETWEEN '2022-10-01 00:00:00' AND '2023-01-31 23:59:59'
                        GROUP BY user_id;"""
        cursor.execute(sql_query)
        result2 = cursor.fetchall()

    except Exception as e:
        connection.rollback()
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    return result, result1, result2

def plot_style():
    plt.rcParams['axes.spines.left'] = False
    plt.rcParams['axes.spines.right'] = False
    plt.rcParams['axes.spines.top'] = False
    plt.rcParams['axes.spines.bottom'] = False
    plt.grid(axis = 'x', color='white')
    plt.gca().set_facecolor((0.9176, 0.9176, 0.9451))
    plt.tick_params(left=False, bottom=False)
    plt.gca().get_yaxis().set_visible(False)

def create_box_plot_1(prices):
    plot_style()
    plt.boxplot(prices, vert=False, widths=0.7, patch_artist=True, boxprops=dict(facecolor='green', color='green'), flierprops=dict(marker='D', markeredgecolor='black',markerfacecolor='grey'))
    plt.xlabel("price")
    plt.show()

def create_box_plot_2(prices):
    plot_style()
    plt.boxplot(prices, vert=False, widths=0.7, showfliers=False, patch_artist=True, boxprops=dict(facecolor='green', color='green'))
    plt.xlabel("price")
    plt.show()


def create_box_plot_3(average_basket_price):
    if not average_basket_price:
        print("Error: no average basket price")
        return

    plot_style()
    plt.boxplot(average_basket_price, vert=False, widths=0.7, showfliers=False,patch_artist=True, boxprops=dict(facecolor='blue', color='blue'))
    plt.show()

def main():
    load_dotenv(os.path.abspath("../../.env"))
    data, price, average_basket_price = get_data()

    count, mean, std, min, q1, q2, q3, max = zip(*data)
    print(f'count: {count[0]}\nmean: {mean[0]}\nstd: {std[0]}\nmin: {min[0]}\nq1: {q1[0]}\nq2: {q2[0]}\nq3: {q3[0]}\nmax: {max[0]}')

    prices = [p[0] for p in price]

    if not prices:
        print("Error: empty prices")
        return

    create_box_plot_1(prices)
    create_box_plot_2(prices)
    create_box_plot_3([row[1] for row in average_basket_price])

if __name__ == "__main__":
    main()