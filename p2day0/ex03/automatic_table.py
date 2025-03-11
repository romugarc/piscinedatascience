import os
import psycopg2
import glob
from dotenv import load_dotenv


load_dotenv(os.path.abspath("../.env"))

def main():
    """
    Creates a postgres table using the data from a CSV
    """


    params = {
        'dbname': os.getenv("POSTGRES_DB"),
        'user': os.getenv("POSTGRES_USER"),
        'password': os.getenv("POSTGRES_PASSWORD"),
        'host': os.getenv("HOST"),
        'port': os.getenv("DB_PORT"),
    }
    columns = "event_time, event_type, product_id, price, user_id, user_session"

    paths = glob.glob("../subject/customer/*.csv")
    connection = psycopg2.connect(**params)
    cursor = connection.cursor()
    try:
        for path in paths:        
            table_name = path.split('/')[-1].replace('.csv', '')
            create_drop_query = f"""DROP TABLE IF EXISTS {table_name}"""
            cursor.execute(create_drop_query)

            create_table_query = f"""
                    CREATE TABLE IF NOT EXISTS {table_name}(
                        event_time TIMESTAMP,
                        event_type VARCHAR(255),
                        product_id INT,
                        price FLOAT,
                        user_id BIGINT,
                        user_session UUID
                    )"""
            cursor.execute(create_table_query)

            with open(path, 'r') as file:
                next(file)
                cursor.copy_expert(f"COPY {table_name} ({columns}) FROM STDIN WITH CSV", file)
            connection.commit()
            print(f"{table_name} done")
    except Exception as e:
        connection.rollback()
        print(f"Error:{str(e)}")
    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    main()