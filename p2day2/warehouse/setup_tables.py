import os
import psycopg2
import glob
from dotenv import load_dotenv

def create_item_table(cursor, connection):
    path = "../../../../../goinfre/subject/item/item.csv"
    table_name = path.split('/')[-1].replace('.csv', '')
    columns = "product_id, category_id, category_code, brand"
    create_drop_query = f"""DROP TABLE IF EXISTS {table_name}"""
    cursor.execute(create_drop_query)
    create_table_query = f"""CREATE TABLE IF NOT EXISTS {table_name}(
                        product_id INT,
                        category_id BIGINT,
                        category_code TEXT,
                        brand VARCHAR(255) NULL)"""
    cursor.execute(create_table_query)
    with open(path, 'r') as file:
        next(file)
        cursor.copy_expert(f"COPY {table_name} ({columns}) FROM STDIN WITH CSV", file)
    connection.commit()
    print(f"{table_name} done")


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
    try:
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()

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
        create_item_table(cursor, connection)
    except Exception as e:
        connection.rollback()
        print(f"Error:{str(e)}")
    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    main()