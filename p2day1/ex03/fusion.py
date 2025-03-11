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
    columns = "event_type, product_id, prise, user_id, user_session"
    connection = psycopg2.connect(**params)
    cursor = connection.cursor()
    try:
        delete_duplicates_query = f"""CREATE TABLE IF NOT EXISTS temp_table AS
                        SELECT DISTINCT ON ({columns}, DATE_TRUNC('second', event_time)) *
                        FROM (
                            SELECT customers.*,
                            LAG(event_time) OVER (PARTITION BY {columns} ORDER BY event_time) as prev_time
                            FROM customers 
                        ) as subq
                        WHERE 
                            prev_time IS NULL OR 
                            event_time - prev_time > INTERVAL '1 second'
                        ORDER BY {columns}, DATE_TRUNC('second', event_time), event_time
                        """
        connection.execute(delete_duplicates_query)

        drop_query = f"""DROP TABLE IF EXISTS customers"""
        cursor.execute(drop_query)

        alter_query = f"""ALTER TABLE temp_table RENAME TO customers"""
        cursor.execute(alter_query)
        cursor.commit()
        print("removed duplicates in customers")
    except Exception as e:
        connection.rollback()
        print(f"Error:{str(e)}")
    finally:
        cursor.close()
        connection.close()
if __name__ == "__main__":
    main()