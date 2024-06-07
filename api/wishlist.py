import psycopg2
from .db import get_db_connection


class Wishlist:
    @staticmethod
    def get_all():
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM wishlists")
        wishlists = cur.fetchall()
        cur.close()
        conn.close()
        return wishlists

    @staticmethod
    def create(user_account_id):
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(
            "INSERT INTO wishlists (id_useraccount) VALUES (%s) RETURNING *",
            (user_account_id,)
        )
        wishlist = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return wishlist
