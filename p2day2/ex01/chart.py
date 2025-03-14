import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from datetime import datetime


def bar_graph(bardf):
    """
    Creates a bar graph that displays the total amount of purchases per month from Oct 2022 to Jan 2023
    """

    months = [datetime.strptime(m, '%Y-%m').strftime('%b') for m in bardf['to_char']]
    plt.ylabel('total sales in million of A')
    plt.grid(axis = 'y', color='white')
    plt.bar(months, bardf['sum'], zorder=2)
    ax = plt.gca()
    ax.set_facecolor('#EAEAF2')
    ax.yaxis.get_offset_text().set_visible(False)
    plt.grid(axis='y', color='w')
    plt.show()


def fill_graph(filldf):
    """
    Creates a graph that displays the average spend/customer
    """
    regroup_days = [datetime.strptime(day, '%Y-%m-%d') for day in filldf['to_char']]
    plt.ylabel('average spend/customers in A')
    plt.plot(regroup_days, filldf['?column?'], zorder=2)
    plt.fill_between(regroup_days, filldf['?column?'], zorder=2)
    ax = plt.gca()
    ax.set_facecolor('#EAEAF2')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
    ax.yaxis.get_offset_text().set_visible(False)
    plt.grid(color='w')
    plt.xlim(regroup_days[0], regroup_days[-1])
    plt.ylim(0, max(filldf['?column?']) + 5)
    plt.show()



def line_graph(linedf):
    """
    Creates a line graph that displays the number of customers every day from Oct 2022 to Jan 2023
    """
    newdf = linedf.value_counts('date')
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
    Create multiple graphs using the data from the warehouse
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
        linedf = pd.read_sql_query("""SELECT date(event_time),  COUNT(*) OVER (PARTITION BY date(event_time))
                               FROM customers 
                               WHERE event_type = 'purchase' 
                               GROUP BY event_time""", engine)

        bardf = pd.read_sql_query("""SELECT TO_CHAR(event_time, 'YYYY-MM'), SUM(price)
                            FROM customers
                            WHERE event_type = 'purchase' 
                            GROUP BY TO_CHAR(event_time, 'YYYY-MM') 
                            ORDER BY TO_CHAR(event_time, 'YYYY-MM')""", engine)

        filldf = pd.read_sql_query(""" SELECT TO_CHAR(event_time, 'YYYY-MM-DD'), SUM(price) / COUNT(DISTINCT user_id)
                               FROM customers
                               WHERE event_type = 'purchase'
                               GROUP BY TO_CHAR(event_time, 'YYYY-MM-DD')
                               ORDER BY TO_CHAR(event_time, 'YYYY-MM-DD')""", engine)
        line_graph(linedf)
        bar_graph(bardf)
        fill_graph(filldf)

    except Exception as e:
        print(f"Error:{str(e)}")


if __name__ == "__main__":
    main()