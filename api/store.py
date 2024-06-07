import psycopg2
from api.db import get_db_connection


class Store:
    @staticmethod
    def get_all():
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM store;")
        stores = cur.fetchall()
        cur.close()
        conn.close()
        return stores

    @staticmethod
    def create(name, location):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO store (name, location) VALUES (%s, %s) RETURNING *;",
            (name, location)
        )
        store = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return store

    @staticmethod
    def get_by_id(store_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM store WHERE id_store = %s;", (store_id,))
        store = cur.fetchone()
        cur.close()
        conn.close()
        return store

    @staticmethod
    def update(store_id, name, location):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "UPDATE store SET name = %s, location = %s WHERE id_store = %s RETURNING *;",
            (name, location, store_id)
        )
        store = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return store

    @staticmethod
    def delete(store_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM store WHERE id_store = %s RETURNING *;", (store_id,))
        store = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return store
