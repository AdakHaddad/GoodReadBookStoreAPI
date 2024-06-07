import psycopg2
from .db import get_db_connection


class OnlineStore:
    @staticmethod
    def get_all():
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM onlinestore;")
        onlinestores = cur.fetchall()
        cur.close()
        conn.close()
        return onlinestores

    @staticmethod
    def create(name, website, phone):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO onlinestore (store_name, website, phone) VALUES (%s, %s, %s) RETURNING *;",
            (name, website, phone)
        )
        onlinestore = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return onlinestore

    @staticmethod
    def get_by_id(onlinestore_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM onlinestore WHERE store_number = %s;", (onlinestore_id,))
        onlinestore = cur.fetchone()
        cur.close()
        conn.close()
        return onlinestore

    @staticmethod
    def update(onlinestore_id, name, website, phone):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "UPDATE onlinestore SET store_name = %s, website = %s, phone = %s WHERE store_number = %s RETURNING *;",
            (name, website, phone, onlinestore_id)
        )
        onlinestore = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return onlinestore

    @staticmethod
    def delete(onlinestore_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM onlinestore WHERE store_number = %s RETURNING *;", (onlinestore_id,))
        onlinestore = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return onlinestore
