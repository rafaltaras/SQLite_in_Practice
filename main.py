import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def create_table(conn, sql):
    try:
        c = conn.cursor()
        c.execute(sql)
        conn.commit() 
        conn.close()
        return 
    except Error as e:
            print(e)


def add_customer(conn, sql):
    try:
        add_customer =  """INSERT INTO customers (customer_id, FirstName, LastName, Company, Address, City, Email )
            VALUES (?,?,?,?,?,?,?)"""
        c = conn.cursor()
        c.execute(add_customer, sql)
        conn.commit() 
        conn.close()
        return 
    except Error as e:
            print(e)


if __name__ == "__main__":
        create_customers_sql = """
        CREATE TABLE IF NOT EXISTS customers (
            id integer PRIMARY KEY,
            customer_id integer NOT NULL,
            FirstName NVARCHAR(40) NOT NULL,
            LastName  NVARCHAR(20) NOT NULL,
            Company  NVARCHAR(80),
            Address  NVARCHAR(70),
            City     NVARCHAR(40),
            Email    NVARCHAR(60)
        );
        """


db_file = "database/database.db"

conn = create_connection(db_file)
# create_table(conn, create_customers_sql)

customers = (2,"Paweł","Taraska","Orange","Al. Jerozolimskie 160","Warszawa","pawel.taraska@orange.com")
add_customer(conn, customers)