import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import pandas as pd


def price_graph(pricedf):
    plt.ylabel("price")
    plt.boxplot(pricedf['price'], vert=False, widths=0.7, flierprops=dict(marker='D', markeredgecolor='black',markerfacecolor='grey'))
    ax = plt.gca()
    ax.set_facecolor('#EAEAF2')
    ax.get_yaxis().set_visible(False)
    plt.grid(axis='x', color='w')
    plt.show()


def price_graph2(pricedf):
    plt.ylabel("price")
    plt.boxplot(pricedf['price'], vert=False, widths=0.7, showfliers=False, patch_artist=True, boxprops=dict(facecolor='g', color='g'))
    ax = plt.gca()
    ax.set_facecolor('#EAEAF2')
    ax.get_yaxis().set_visible(False)
    plt.grid(axis='x', color='w')
    plt.show()


def basket_graph(basketdf):
    plt.boxplot(basketdf['avg'], vert=False, widths=0.7, patch_artist=True, boxprops=dict(facecolor='b', color='b'))
    ax = plt.gca()
    ax.set_facecolor('#EAEAF2')
    ax.get_yaxis().set_visible(False)
    plt.xticks(range(26, 44, 2))
    plt.grid(axis='x', color='w')
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

        pricedf = pd.read_sql_query(""" SELECT price
                                        FROM customers
                                        WHERE event_type = 'purchase'""", engine)
        
        basketdf = pd.read_sql_query("""SELECT user_id, AVG(price)
                                        FROM customers
                                        WHERE event_type = 'cart'
                                        GROUP BY user_id
                                        HAVING AVG(price) BETWEEN 26 AND 43""", engine)
        print(pricedf.describe().apply(lambda s: s.apply('{0:.5f}'.format)))
        price_graph(pricedf)
        price_graph2(pricedf)
        basket_graph(basketdf)


    except Exception as e:
        print(f"Error:{str(e)}")

if __name__ == "__main__":
    main()