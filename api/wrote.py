import psycopg2
from api.db import get_db_connection


class Wrote:
    @staticmethod
    def get_all():
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM wrote;")
        wrotes = cur.fetchall()
        cur.close()
        conn.close()
        return wrotes

    @staticmethod
    def create(book_number, author_number):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO wrote (book_number, author_number) VALUES (%s, %s) RETURNING *;",
            (book_number, author_number)
        )
        wrote = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return wrote

    @staticmethod
    def get_by_id(wrote_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM wrote WHERE id_wrote = %s;", (wrote_id,))
        wrote = cur.fetchone()
        cur.close()
        conn.close()
        return wrote

    @staticmethod
    def update(wrote_id, book_number, author_number):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "UPDATE wrote SET book_number = %s, author_number = %s WHERE id_wrote = %s RETURNING *;",
            (book_number, author_number, wrote_id)
        )
        wrote = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return wrote

    @staticmethod
    def delete(wrote_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM wrote WHERE id_wrote = %s RETURNING *;", (wrote_id,))
        wrote = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return wrote
