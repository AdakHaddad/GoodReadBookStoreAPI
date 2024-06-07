import psycopg2
from .db import get_db_connection


class Customer:
    @staticmethod
    def get_all():
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM customer;")
        customers = cur.fetchall()
        cur.close()
        conn.close()
        return customers

    @staticmethod
    def create(name, street, city, state, country):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO customer (customer_name, street, city, state, country) VALUES (%s, %s, %s, %s, %s) RETURNING *;",
            (name, street, city, state, country)
        )
        customer = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return customer

    @staticmethod
    def get_by_id(customer_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM customer WHERE customer_number = %s;", (customer_id,))
        customer = cur.fetchone()
        cur.close()
        conn.close()
        return customer

    @staticmethod
    def update(customer_id, name, street, city, state, country):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "UPDATE customer SET customer_name = %s, street = %s, city = %s, state = %s, country = %s WHERE customer_number = %s RETURNING *;",
            (name, street, city, state, country, customer_id)
        )
        customer = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return customer

    @staticmethod
    def delete(customer_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM customer WHERE customer_number = %s RETURNING *;", (customer_id,))
        customer = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return customer
