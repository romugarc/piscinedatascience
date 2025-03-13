import os
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

def line_graph(timedf):
    """
    Creates a line graph that displays the number of customers every day from Oct 2022 to Jan 2023
    """
    newdf = timedf.value_counts('date')
    newdf = newdf.sort_index()
    plt.ylabel("Number of customers")
    plt.plot(newdf)
    ax = plt.gca()
    ax.set_facecolor('#EAEAF2')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
    plt.xlim(newdf.index[0], newdf.index[-1])
    plt.grid(color='w')
    plt.show()


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
        timedf = pd.read_sql_query("""SELECT date(event_time),  COUNT(*) OVER (PARTITION BY date(event_time)) FROM customers WHERE event_type = 'purchase' GROUP BY event_time""", engine)
        line_graph(timedf)


    except Exception as e:
        print(f"Error:{str(e)}")


if __name__ == "__main__":
    main()