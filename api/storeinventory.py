import psycopg2
from api.db import get_db_connection


class StoreInventory:
    @staticmethod
    def get_all():
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM storeinventory;")
        storeinventories = cur.fetchall()
        cur.close()
        conn.close()
        return storeinventories

    @staticmethod
    def create(store_number, book_number, quantity):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO storeinventory (store_number, book_number, quantity) VALUES (%s, %s, %s) RETURNING *;",
            (store_number, book_number, quantity)
        )
        storeinventory = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return storeinventory

    @staticmethod
    def get_by_id(storeinventory_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM storeinventory WHERE id_storeinventory = %s;", (storeinventory_id,))
        storeinventory = cur.fetchone()
        cur.close()
        conn.close()
        return storeinventory

    @staticmethod
    def update(storeinventory_id, store_number, book_number, quantity):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "UPDATE storeinventory SET store_number = %s, book_number = %s, quantity = %s WHERE id_storeinventory = %s RETURNING *;",
            (store_number, book_number, quantity, storeinventory_id)
        )
        storeinventory = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return storeinventory

    @staticmethod
    def delete(storeinventory_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM storeinventory WHERE id_storeinventory = %s RETURNING *;", (storeinventory_id,))
        storeinventory = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return storeinventory
