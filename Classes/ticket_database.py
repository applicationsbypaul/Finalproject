"""
Program: ticket_databse.py
Author: Paul Ford
Last date modified: 08/1/2020
Purpose: creates an a db object
         and manipulate data with
         with definitions.
"""
import sqlite3


def create_connection(db):
    """ Connect to a SQLite database
    :param db: filename of database
    :return connection if no error, otherwise None"""
    try:
        conn = sqlite3.connect(db)
        print(sqlite3.version)
        return conn
    except sqlite3.Error as err:
        print(err)
    return None

def create_table(conn):
    sql_create_tickets_table = """ CREATE TABLE IF NOT EXISTS tickets (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """
    try:
        c = conn.cursor()
        c.execute(sql_create_tickets_table)
    except sqlite3.Error as e:
        print(e)

def add_ticket(conn, ticket):
    """Create a new person for table
    :param conn:
    :param ticket:
    :return: ticket id
    """
    sql = ''' INSERT INTO tickets(name,description,storeID,priority,status,date)
              VALUES(?,?,?,?,?,?,?) '''
    cur = conn.cursor()  # cursor object
    cur.execute(sql, ticket)
    return cur.lastrowid  # returns the row id of the cursor object, the ticket id


# def create_student(conn, student):
#   """Create a new person for table
#    :param conn:
#   :param student:
#   :return: student id
#   """
#   sql = ''' INSERT INTO student(id, major, begin_date)
#             VALUES(?,?,?) '''
#   cur = conn.cursor()  # cursor object
#   cur.execute(sql, student)
#   return cur.lastrowid  # returns the row id of the cursor object, the student id


def select_all_tickets(conn):
    """Query all rows of person table
    :param conn: the connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM ticket")

    rows = cur.fetchall()

    return rows  # return the rows


def delete_ticket(conn, id):
    """Delete a person by person id
    :param conn: database connection
    :param id: id of the person
    :return:
    """
    sql = 'DELETE FROM person WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))


if __name__ == '__main__':
    conn = create_connection('ticketsdb.db')
    create_table(conn)
