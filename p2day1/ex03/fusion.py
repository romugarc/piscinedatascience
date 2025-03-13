import psycopg2
import os
from dotenv import load_dotenv


def main():
    """
    Creates a postgres table using the data from a CSV
    """
    load_dotenv(os.path.abspath("../.env"))

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

        columns = ["category_id", "category_code", "brand"]
        types = ["BIGINT", "TEXT", "VARCHAR(255) NULL"]
        for item, type in zip(columns, types):
            alter_query = f"""ALTER TABLE customers ADD COLUMN IF NOT EXISTS {item} {type}"""
            cursor.execute(alter_query)
        
        temp_query = """
                    CREATE TABLE temp_table AS
                    SELECT
                        product_id,
                        MAX(category_id) AS category_id,
                        MAX(category_code) AS category_code,
                        MAX(brand) AS brand
                    FROM item
                    GROUP BY product_id"""
        cursor.execute(temp_query)

        drop_query = """DROP TABLE IF EXISTS item"""
        cursor.execute(drop_query)

        alter_query = """ALTER TABLE temp_table RENAME TO item"""
        cursor.execute(alter_query)

        fusion_query = f"""
                UPDATE customers
                SET 
                    category_id = item.category_id,
                    category_code = item.category_code,
                    brand = item.brand
                FROM item
                WHERE customers.product_id = item.product_id"""
        cursor.execute(fusion_query)
        connection.commit()
        print("fusion customers + item done")
    except Exception as e:
        connection.rollback()
        print(f"Error:{str(e)}")
    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    main()