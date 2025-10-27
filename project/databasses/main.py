import config
import psycopg2

with psycopg2.connect(
        dbname=config.PGDATABASE,
        user=config.PGUSER,
        password=config.PGPASSWORD,
        host=config.PGHOST,
        port=5432,
) as connection:
    with connection.cursor() as cursor:
        query_topics = """
                    CREATE TABLE IF NOT EXISTS topics (
                        id SERIAL PRIMARY KEY,
                        title VARCHAR(100) NOT NULL UNIQUE,
                        description TEXT
                    );
                """
        cursor.execute(query_topics)

        query_users = """
                    CREATE TABLE IF NOT EXISTS users (
                        id SERIAL PRIMARY KEY,
                        username VARCHAR(50) NOT NULL UNIQUE,
                        email VARCHAR(75) NOT NULL,
                        registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                """
        cursor.execute(query_users)

        query_posts = """
                    CREATE TABLE IF NOT EXISTS posts (
                        id SERIAL PRIMARY KEY,
                        content TEXT NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        user_id INTEGER REFERENCES users(id),
                        topic_id INTEGER REFERENCES topics(id)
                    );
                """
        cursor.execute(query_posts)



# CREATE
with psycopg2.connect(
        dbname=config.PGDATABASE,
        user=config.PGUSER,
        password=config.PGPASSWORD,
        host=config.PGHOST,
        port=5432,
) as connection:
    with connection.cursor() as cursor:
        query_customer = 'INSERT INTO customer (name) VALUES (%s) RETURNING id'
        cursor.execute(query_customer, ('Sashka',))
        customer_id = cursor.fetchone()[0]

        query_brand = 'INSERT INTO brand (name) VALUES (%s) RETURNING id'
        cursor.execute(query_brand, ('Toyota',))
        brand_id = cursor.fetchone()[0]

        query_car = 'INSERT INTO car (model, brand_id, customer_id) VALUES (%s, %s, %s)'
        cursor.execute(query_car, ('Prius', brand_id, customer_id))

        connection.commit()
