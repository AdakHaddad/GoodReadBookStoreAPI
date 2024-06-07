import psycopg2

from .db import get_db_connection


class Review:
    @staticmethod
    def get_all():
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM review;")
        reviews = cur.fetchall()
        cur.close()
        conn.close()
        return reviews

    @staticmethod
    def create(book_number, customer_number, review, rating):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO review (book_number, customer_number, review, rating) VALUES (%s, %s, %s, %s) RETURNING *;",
            (book_number, customer_number, review, rating)
        )
        review = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return review

    @staticmethod
    def get_by_id(review_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM review WHERE review_number = %s;", (review_id,))
        review = cur.fetchone()
        cur.close()
        conn.close()
        return review

    @staticmethod
    def update(review_id, book_number, customer_number, review, rating):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "UPDATE review SET book_number = %s, customer_number = %s, review = %s, rating = %s WHERE review_number = %s RETURNING *;",
            (book_number, customer_number, review, rating, review_id)
        )
        review = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return review

    @staticmethod
    def delete(review_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM review WHERE review_number = %s RETURNING *;", (review_id,))
        review = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return review
