# useraccount.py
import psycopg2
from .db import get_db_connection


class UserAccount:
    @staticmethod
    def get_all():
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM useraccount")
        useraccounts = cur.fetchall()
        cur.close()
        conn.close()
        return useraccounts

    @staticmethod
    def get_by_id(user_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM useraccount WHERE user_id = %s", (user_id,))
        useraccount = cur.fetchone()
        cur.close()
        conn.close()
        return useraccount
