import psycopg2
from .db import get_db_connection


class Author:
    @staticmethod
    def get_all():
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM authors")
        authors = cur.fetchall()
        cur.close()
        conn.close()
        return authors

    @staticmethod
    def create(number, name, year_born, year_died=None):
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(
            "INSERT INTO authors (author_number,author_name, year_born, year_died) VALUES (%s, %s, %s) RETURNING *",
            (number, name, year_born, year_died)
        )
        author = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return author
