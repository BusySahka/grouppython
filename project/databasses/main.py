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
        query_insert = 'INSERT INTO topics (title, description) VALUES (%s, %s)'
        cursor.execute(query_insert, ("School", "All about solving math problems"))
        cursor.execute(query_insert, ("Sport", "How not to lose motivation"))
        cursor.execute(query_insert, ("Programming", "Is it really that hard?"))