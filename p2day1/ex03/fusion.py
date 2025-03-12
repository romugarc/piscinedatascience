import psycopg2
import os
from dotenv import load_dotenv

def change_item_table(cursor):
    sql_query = """
            CREATE TABLE temp_item AS
            SELECT
                product_id,
                MAX(category_id) AS category_id,
                MAX(category_code) AS category_code,
                MAX(brand) AS brand
            FROM item
            GROUP BY product_id;
            """
    cursor.execute(sql_query)

    sql_query = """DROP TABLE IF EXISTS item;"""
    cursor.execute(sql_query)

    sql_query = """ALTER TABLE temp_item RENAME TO item;"""
    cursor.execute(sql_query)

def fusion_tables():
    connection_params = {
        'dbname': os.getenv("POSTGRES_DB"),
        'user': os.getenv("POSTGRES_USER"),
        'password': os.getenv("POSTGRES_PASSWORD"),
        'host': os.getenv("HOST"),
        'port': os.getenv("POSTGRES_PORT")
    }

    try:
        connection = psycopg2.connect(**connection_params)
        cursor = connection.cursor()

        change_item_table(cursor)

        sql_query = """
        CREATE TABLE IF NOT EXISTS temp_customers AS
        SELECT customers.*, item.category_id, item.category_code, item.brand
        FROM customers
        LEFT JOIN item
        ON customers.product_id = item.product_id;"""
        cursor.execute(sql_query)

        sql_query = """
               DROP TABLE IF EXISTS customers;"""
        cursor.execute(sql_query)

        sql_query = """
        ALTER TABLE temp_customers RENAME TO customers;"""
        cursor.execute(sql_query)

        connection.commit()
    except psycopg2.Error as e:
        print(f"Database error: {e}")
        if connection:
            connection.rollback()
    except Exception as e:
        if connection:
            connection.rollback()
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def main():
    load_dotenv(os.path.abspath("../.env"))
    fusion_tables()


if __name__ == "__main__":
    main()