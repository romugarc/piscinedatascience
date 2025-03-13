import os
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import pandas as pd


def main():
    """
    Create a pie chart using the data from the warehouse
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
        #timedf = pd.read_sql_query("""SELECT CAST(event_time as date), user_id FROM customers WHERE event_type = 'purchase'""", engine)
        timedf = pd.read_sql_query("""SELECT date(event_time),  COUNT(*) OVER (PARTITION BY date(event_time)) FROM customers WHERE event_type = 'purchase' GROUP BY event_time""", engine)
        print(timedf)
        newdf = timedf.value_counts('date')
        print(newdf)
        newdf = newdf.sort_index()
        plt.ylabel("Number of customers")
        plt.plot(newdf)
        ax = plt.gca()
        ax.set_facecolor('#EAEAF2')
        plt.grid(color='w')
        plt.show()

    except Exception as e:
        print(f"Error:{str(e)}")


if __name__ == "__main__":
    main()