import psycopg2
from psycopg2.extras import RealDictCursor
from flask import Flask, request, jsonify


def get_db_connection():
    conn = psycopg2.connect(
        "postgresql://postgres:ASDFGHJKL;'@localhost:1030/grb_db"
    )
    return conn


class Table:

    @staticmethod
    def get_all():
        conn = Table.get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM your_table")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows

    @staticmethod
    def get_by_id(row_id):
        conn = Table.get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM your_table WHERE id = %s", (row_id,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row

    @staticmethod
    def create(column1, column2, column3):
        conn = Table.get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO your_table (column1, column2, column3) VALUES (%s, %s, %s) RETURNING *",
                    (column1, column2, column3))
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return row

    @staticmethod
    def update(row_id, column1, column2, column3):
        conn = Table.get_db_connection()
        cur = conn.cursor()
        cur.execute("UPDATE your_table SET column1 = %s, column2 = %s, column3 = %s WHERE id = %s RETURNING *",
                    (column1, column2, column3, row_id))
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return row

    @staticmethod
    def delete(row_id):
        conn = Table.get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM your_table WHERE id = %s RETURNING *", (row_id,))
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return row


class Database:
    @staticmethod
    def get_all_table_names():
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
            AND table_type = 'BASE TABLE';
        """)
        tables = cur.fetchall()
        cur.close()
        conn.close()
        return [table[0] for table in tables]


def execute_transaction(queries):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        for query in queries:
            cur.execute(*query)
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cur.close()
        conn.close()
