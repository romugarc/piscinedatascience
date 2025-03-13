import os
import psycopg2
import glob
from dotenv import load_dotenv


def main():
    """
    Creates a postgres table using the data from a CSV
    """
    load_dotenv(os.path.abspath("../.env"))

    params = {
        'dbname': os.getenv("POSTGRES_DB"),
        'user': os.getenv("POSTGRES_USER"),
        'password': os.getenv("POSTGRES_PASSWORD"),
        'host': os.getenv("HOST"),
        'port': os.getenv("DB_PORT"),
    }
    columns = "event_time, event_type, product_id, price, user_id, user_session"

    paths = glob.glob("../../../../../goinfre/subject/customer/*.csv")
    union_queries = []
    try:
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()

        for path in paths:
            table_name = path.split('/')[-1].replace('.csv', '')
            union_queries.append(f"SELECT * FROM {table_name}")

        union_query = " UNION ALL ".join(union_queries)
        create_drop_query = f"""DROP TABLE IF EXISTS customers"""
        cursor.execute(create_drop_query)

        create_union_query = f"""CREATE TABLE IF NOT EXISTS customers AS {union_query}"""
        cursor.execute(create_union_query)
        connection.commit()
        print(f"customers table done")
    except Exception as e:
        connection.rollback()
        print(f"Error:{str(e)}")
    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    main()