import os
import psycopg2
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
        df = pd.read_sql_query("""SELECT (event_type) FROM customers""", engine)
        newdf = df.value_counts()
        labels = [str(item).strip("(',)") for item in newdf.keys()]
        explode = [0.01, 0.01, 0.01, 0.01]

        plt.pie(newdf, labels=labels, autopct='%1.1f%%', explode=explode)
        plt.show()
    except Exception as e:
        print(f"Error:{str(e)}")


if __name__ == "__main__":
    main()