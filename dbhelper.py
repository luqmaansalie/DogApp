import sqlite3
import traceback


def init_db():
    conn = sqlite3.connect('database.db')
    conn.execute('CREATE TABLE dogs (id INTEGER PRIMARY KEY, name TEXT)')
    conn.close()


def read_all():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row

    cur = conn.cursor()
    cur.execute("select * from dogs")

    return cur.fetchall()


def read(id):
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row

    cur = conn.cursor()
    cur.execute("select * from dogs where id = ?", [id])

    return cur.fetchall()


def read_one():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row

    cur = conn.cursor()
    cur.execute("SELECT * FROM dogs LIMIT 1")

    return cur.fetchone()


def insert(id, name):
    try:
        with sqlite3.connect("database.db") as con:
            cur = con.cursor()

            cur.execute("select count(*) from dogs where id = ?", [id])
            data = cur.fetchone()[0]
            msg = "ID exists"

            if data == 0:
                cur.execute("INSERT INTO dogs (id, name) VALUES (?, ?)", (id, name))
                con.commit()
                msg = "Record successfully added"
    except:
        con.rollback()
        traceback.print_exc()
        msg = "error in insert operation"

    finally:
        con.close()
        return msg


def update(id, name):
    try:
        with sqlite3.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("update dogs set name = ? where id = ?", (name, id))
            con.commit()
            msg = "Record successfully updated"
    except:
        con.rollback()
        traceback.print_exc()
        msg = "error in update operation"

    finally:
        con.close()
        return msg


def delete(id):
    try:
        with sqlite3.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("delete from dogs where id = ?", [id])
            con.commit()
            msg = "Record successfully deleted"
    except:
        con.rollback()
        traceback.print_exc()
        msg = "error in delete operation"

    finally:
        con.close()
        return msg
