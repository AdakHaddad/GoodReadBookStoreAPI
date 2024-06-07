# category.py
import psycopg2
from .db import get_db_connection


class Category:
    @staticmethod
    def get_all():
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM category")
        categories = cur.fetchall()
        cur.close()
        conn.close()
        return categories

    @staticmethod
    def get_by_id(category_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM category WHERE category_id = %s", (category_id,))
        category = cur.fetchone()
        cur.close()
        conn.close()
        return category
