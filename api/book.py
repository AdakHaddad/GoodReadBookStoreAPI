import psycopg2
from .db import get_db_connection


class Book:
    @staticmethod
    def get_all():
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM book;")
        books = cur.fetchall()
        cur.close()
        conn.close()
        return books

    @staticmethod
    def create(book_name, publication_year, pages, id_publisher, id_category):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO book (book_name, publication_year, pages, id_publisher, id_category) VALUES (%s, %s, %s, %s, %s) RETURNING *;",
            (book_name, publication_year, pages, id_publisher, id_category)
        )
        book = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return book

    @staticmethod
    def get_by_id(book_number):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM book WHERE book_number = %s;",
                    (book_number,))
        book = cur.fetchone()
        cur.close()
        conn.close()
        return book

    @staticmethod
    def update(book_number, book_name, publication_year, pages, id_publisher, id_category):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "UPDATE book SET book_name = %s, publication_year = %s, pages = %s, id_publisher = %s, id_category = %s WHERE book_number = %s RETURNING *;",
            (book_name, publication_year, pages,
             id_publisher, id_category, book_number)
        )
        book = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return book

    @staticmethod
    def delete(book_number):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM book WHERE book_number = %s RETURNING *;", (book_number,))
        book = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return book
