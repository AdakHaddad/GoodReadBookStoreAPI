import psycopg2
from api.db import get_db_connection


class Staff:
    @staticmethod
    def get_all():
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM staff;")
        staff_members = cur.fetchall()
        cur.close()
        conn.close()
        return staff_members

    @staticmethod
    def create(staff_name, email, role, store_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO staff (staff_name, email, role, store_id) VALUES (%s, %s, %s, %s) RETURNING *;",
            (staff_name, email, role, store_id)
        )
        staff_member = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return staff_member

    @staticmethod
    def get_by_id(staff_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM staff WHERE staff_id = %s;", (staff_id,))
        staff_member = cur.fetchone()
        cur.close()
        conn.close()
        return staff_member

    @staticmethod
    def update(staff_id, staff_name, email, role, store_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "UPDATE staff SET staff_name = %s, email = %s, role = %s, store_id = %s WHERE staff_id = %s RETURNING *;",
            (staff_name, email, role, store_id, staff_id)
        )
        staff_member = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return staff_member

    @staticmethod
    def delete(staff_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM staff WHERE staff_id = %s RETURNING *;", (staff_id,))
        staff_member = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return staff_member
