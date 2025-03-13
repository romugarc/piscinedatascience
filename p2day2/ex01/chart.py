import os
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

def bar_graph(timedf):
    """
    Creates a bar graph that displays the total amount of purchases per month from Oct 2022 to Jan 2023
    """
    #month, amount = zip(*data)
    #formatted_months = [datetime.strptime(m, '%Y-%m').strftime('%b') for m in month]

    #plt.rcParams['axes.spines.left'] = False
    #plt.rcParams['axes.spines.right'] = False
    #plt.rcParams['axes.spines.top'] = False
    #plt.rcParams['axes.spines.bottom'] = False
    #if grid:
    #    plt.grid(True, color='white')
    #else:
    #    plt.grid(axis = 'y', color='white')
    #plt.gca().set_facecolor((0.9176, 0.9176, 0.9451))
    #plt.tick_params(left=False, bottom=False)

    #plt.bar(formatted_months, amount, color='#B9C4D6', edgecolor='white', zorder=3)

    #ax = plt.gca()
    #ax.yaxis.get_offset_text().set_visible(False)
    #plt.ylabel('total sales in million of A')

    #plt.show()


def fill_graph(timedf):
    """
    Creates a graph that displays the average spend/customer
    """
    #purchase_day, average_spend_per_customer_per_day = zip(*data)
    #purchase_day = [datetime.strptime(day, '%Y-%m-%d') for day in purchase_day]

    #plt.rcParams['axes.spines.left'] = False
    #plt.rcParams['axes.spines.right'] = False
    #plt.rcParams['axes.spines.top'] = False
    #plt.rcParams['axes.spines.bottom'] = False
    #if grid:
    #    plt.grid(True, color='white')
    #else:
    #    plt.grid(axis = 'y', color='white')
    #plt.gca().set_facecolor((0.9176, 0.9176, 0.9451))
    #plt.tick_params(left=False, bottom=False)

    #plt.plot(purchase_day, average_spend_per_customer_per_day, color='#B9C4D6', zorder=3)
    #plt.fill_between(purchase_day, average_spend_per_customer_per_day, color='#B9C4D6', zorder=3)

    #plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    #plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))

    #plt.ylabel('average spend/customers in A')

    #plt.xlim(purchase_day[0], purchase_day[-1])
    #plt.ylim(0, max(average_spend_per_customer_per_day) + 5)

    #plt.show()



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
        df = pd.read_sql_query("""SELECT date(event_time),  COUNT(*) OVER (PARTITION BY date(event_time))
                               FROM customers 
                               WHERE event_type = 'purchase' 
                               GROUP BY event_time""", engine)
        line_graph(df)

        df = pd.read_sql_query("""SELECT TO_CHAR(event_time, 'YYYY-MM'), SUM(price)
                            FROM customers
                            WHERE event_type = 'purchase' 
                            GROUP BY TO_CHAR(event_time, 'YYYY-MM') 
                            ORDER BY purchase_month""", engine)
        bar_graph(df)

        df = pd.read_sql_query(""" SELECT TO_CHAR(event_time, 'YYYY-MM-DD'), SUM(price) / COUNT(DISTINCT user_id)
                               FROM customers
                               WHERE event_type = 'purchase'
                               GROUP BY TO_CHAR(event_time, 'YYYY-MM-DD')
                               ORDER BY purchase_day""", engine)
        fill_graph(df)
        

    except Exception as e:
        print(f"Error:{str(e)}")


if __name__ == "__main__":
    main()