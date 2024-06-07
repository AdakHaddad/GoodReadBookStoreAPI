import psycopg2

from .db import get_db_connection


class WishlistItem:
    @staticmethod
    def get_all():
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM wishlistitem;")
        wishlistitems = cur.fetchall()
        cur.close()
        conn.close()
        return wishlistitems

    @staticmethod
    def create(wishlist_number, book_number):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO wishlistitem (wishlist_number, book_number) VALUES (%s, %s) RETURNING *;",
            (wishlist_number, book_number)
        )
        wishlistitem = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return wishlistitem

    @staticmethod
    def get_by_id(wishlistitem_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM wishlistitem WHERE id_wishlistitem = %s;", (wishlistitem_id,))
        wishlistitem = cur.fetchone()
        cur.close()
        conn.close()
        return wishlistitem

    @staticmethod
    def update(wishlistitem_id, wishlist_number, book_number):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "UPDATE wishlistitem SET wishlist_number = %s, book_number = %s WHERE id_wishlistitem = %s RETURNING *;",
            (wishlist_number, book_number, wishlistitem_id)
        )
        wishlistitem = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return wishlistitem

    @staticmethod
    def delete(wishlistitem_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM wishlistitem WHERE id_wishlistitem = %s RETURNING *;", (wishlistitem_id,))
        wishlistitem = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return wishlistitem
