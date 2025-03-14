import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import pandas as pd


def freq_graph(freqdf):
    plt.xlabel("frequency")
    plt.ylabel("customers")
    plt.hist(freqdf['count'], bins=5, range=[0, 40], edgecolor='w', zorder=2)
    plt.xticks(range(0, 40, 10))
    ax = plt.gca()
    ax.set_facecolor('#EAEAF2')
    plt.grid(color='w')
    plt.show()


def money_graph(moneydf):
    plt.xlabel("monetary value in A")
    plt.ylabel("customers")
    plt.hist(moneydf['sum'], bins=5, range=[0, 250], edgecolor='w', zorder=2)
    plt.xticks(range(0, 250, 50))
    ax = plt.gca()
    ax.set_facecolor('#EAEAF2')
    plt.grid(color='w')
    plt.show()


def main():
    """
    Create multiple box charts using the data from the warehouse
    """
    load_dotenv(os.path.abspath("../.env"))
    params = {
        'dbname': os.getenv("POSTGRES_DB"),
        'user': os.getenv("POSTGRES_USER"),
        'password': os.getenv("POSTGRES_PASSWORD"),
        'host': os.getenv("HOST"),
        'port': os.getenv("DB_PORT")
    }
    try:
        engine = create_engine(f"postgresql+psycopg2://{params['user']}:{params['password']}@{params['host']}:{params['port']}/{params['dbname']}")

        freqdf = pd.read_sql_query("""SELECT user_id, COUNT(*)
                                    FROM customers
                                    WHERE event_type = 'purchase'
                                    GROUP BY user_id""", engine)
        
        moneydf = pd.read_sql_query(""" SELECT user_id, SUM(price)
                                      FROM customers
                                      WHERE event_type = 'purchase'
                                      GROUP BY user_id
                                      ORDER BY SUM(price)""", engine)
        freq_graph(freqdf)
        money_graph(moneydf)


    except Exception as e:
        print(f"Error:{str(e)}")

if __name__ == "__main__":
    main()