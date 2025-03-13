import psycopg2
import os
from dotenv import load_dotenv
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
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
    try:

        sql_query = """SELECT user_id, COUNT(*) AS nbr_order
                    FROM customers
                    WHERE event_type = 'purchase'
                    AND event_time BETWEEN '2022-10-01 00:00:00' AND '2023-01-31 23:59:59'
                    GROUP BY user_id;"""

        cursor.execute(sql_query)
        result = cursor.fetchall()

        sql_query = """ SELECT user_id, SUM(price) AS amount
        FROM customers
        WHERE event_type = 'purchase'
        AND event_time BETWEEN '2022-10-01 00:00:00' AND '2023-01-31 23:59:59' 
        GROUP BY user_id
        ORDER BY amount;"""
        cursor.execute(sql_query)
        result1 = cursor.fetchall()
    except Exception as e:
        connection.rollback()
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    return result, result1


def plot_style():
    plt.rcParams['axes.spines.left'] = False
    plt.rcParams['axes.spines.right'] = False
    plt.rcParams['axes.spines.top'] = False
    plt.rcParams['axes.spines.bottom'] = False
    plt.grid(True, color='white')
    plt.gca().set_facecolor((0.9176, 0.9176, 0.9451))
    plt.tick_params(left=False, bottom=False)

def create_frequency_chart(nbr_order):
    plot_style()
    if not nbr_order:
        print("Error: no value")
        return

    plt.hist(nbr_order, bins=5, range=[0, 40], color='#B9C4D6', edgecolor='white', zorder=3)

    plt.xticks(np.arange(10, 40 , 10))
    plt.xlabel("frequency")
    plt.ylabel("customers")

    plt.show()

def create_monetary_value_chart(total_spent):
    if not total_spent:
        print("Error: no value")
        return
    plot_style()
    plt.hist(total_spent, bins=5, range=[0, 250], color='#B9C4D6', edgecolor='white', zorder=3)
    plt.xticks(np.arange(0, 250, 50))
    plt.xlabel("monetary value in A")
    plt.ylabel("customers")
    plt.show()

def main():
    load_dotenv(os.path.abspath("../../.env"))
    data, data1 = get_data()
    user_id, nbr_order = zip(*data)

    create_frequency_chart(nbr_order)
    create_monetary_value_chart([item[1] for item in data1])

if __name__ == "__main__":
    main()