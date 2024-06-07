# publisher.py
import psycopg2
from .db import get_db_connection


class Publisher:
    @staticmethod
    def get_all():
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM publisher")
        publishers = cur.fetchall()
        cur.close()
        conn.close()
        return publishers

    @staticmethod
    def get_by_id(publisher_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM publisher WHERE publisher_id = %s", (publisher_id,))
        publisher = cur.fetchone()
        cur.close()
        conn.close()
        return publisher
