import psycopg2
import os
from dotenv import load_dotenv
import pandas as pd


load_dotenv(os.path.abspath("./.env"))


def create_table_and_copy_data(csv_path: str, table_name: str):
    """
    Creates a table in the PostgreSQL database if it doesn't exist and
    loads the provided DataFrame into it.
    """

    connection_params = {
        'dbname': os.getenv("POSTGRES_DB"),
        'user': os.getenv("POSTGRES_USER"),
        'password': os.getenv("POSTGRES_PASSWORD"),
        'host': os.getenv("HOST"),
        'port': os.getenv("POSTGRES_PORT")
    }

    connection = psycopg2.connect(**connection_params)
    cursor = connection.cursor()

    try:
        create_table_query = f"""
                CREATE TABLE IF NOT EXISTS {table_name}(
                    id SERIAL PRIMARY KEY,
                    product_id INT,
                    category_id BIGINT,
                    category_code VARCHAR(255) NULL,
                    brand VARCHAR(255) NULL
                )"""

        cursor.execute(create_table_query)

        with open(csv_path, 'r') as f:
            next(f)
            columns = "product_id, category_id, category_code, brand"
            cursor.copy_expert(
                f"COPY {table_name} ({columns}) FROM STDIN WITH CSV",
                f
            )

        # delete_null_query = f"DELETE FROM {table_name} WHERE category_id IS NULL AND brand IS NULL AND category_code IS NOT NULL;"
        # cursor.execute(delete_null_query)

        connection.commit()
        print(f"Successfully copied data from {csv_path} to {table_name}")

    except Exception as e:
        connection.rollback()
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()


def main():
    """
     Main function to load data from a CSV file,
     delete the duplicates and insert it into a PostgreSQL table.
    """
    path = "subject/item/item.csv"
    # df = pd.read_csv("subject/item/item.csv")
    #
    # unique_df = df.drop_duplicates()
    #
    # unique_df.to_csv(path, index=False)
    create_table_and_copy_data(path, path.split('/')[-1].replace('.csv', ''))


if __name__ == "__main__":
    main()