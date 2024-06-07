import psycopg2

from api.db import get_db_connection


class Bought:
    @staticmethod
    def get_all():
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM bought;")
        boughts = cur.fetchall()
        cur.close()
        conn.close()
        return boughts

    @staticmethod
    def create(customer_number, book_number, purchase_date, price, quantity):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO bought (customer_number, book_number, purchase_date,price, quantity) VALUES (%s, %s, %s, %s) RETURNING *;",
            (customer_number, book_number, purchase_date, price, quantity)
        )
        bought = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return bought

    @staticmethod
    def get_by_id(bought_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM bought WHERE id_bought = %s;", (bought_id,))
        bought = cur.fetchone()
        cur.close()
        conn.close()
        return bought

    @staticmethod
    def update(bought_id, customer_number, book_number, date, quantity):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "UPDATE bought SET customer_number = %s, book_number = %s, date = %s, quantity = %s WHERE id_bought = %s RETURNING *;",
            (customer_number, book_number, date, quantity, bought_id)
        )
        bought = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return bought

    @staticmethod
    def delete(bought_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM bought WHERE id_bought = %s RETURNING *;", (bought_id,))
        bought = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return bought
