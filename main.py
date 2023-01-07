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

def select_all(conn, table):
   cur = conn.cursor()
   cur.execute(f"SELECT * FROM {table}")
   rows = cur.fetchall()
   return rows

def select_where(conn, table, **query):
   cur = conn.cursor()
   qs = []
   values = ()
   for k, v in query.items():
       qs.append(f"{k}=?")
       values += (v,)
   q = " AND ".join(qs)
   cur.execute(f"SELECT * FROM {table} WHERE {q}", values)
   rows = cur.fetchall()
   return rows

def update(conn, table, id, **kwargs):
   parameters = [f"{k} = ?" for k in kwargs]
   parameters = ", ".join(parameters)
   values = tuple(v for v in kwargs.values())
   values += (id, )
   sql = f''' UPDATE {table}
             SET {parameters}
             WHERE id = ?'''
   try:
       cur = conn.cursor()
       cur.execute(sql, values)
       conn.commit()
       print("ID", id, "updated")
   except sqlite3.OperationalError as e:
       print(e)

def delete_where(conn, table, **kwargs):
   qs = []
   values = tuple()
   for k, v in kwargs.items():
       qs.append(f"{k}=?")
       values += (v,)
   q = " AND ".join(qs)
   sql = f'DELETE FROM {table} WHERE {q}'
   cur = conn.cursor()
   cur.execute(sql, values)
   conn.commit()
   print("Deleted")

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

# customers = (3,"Łukasz","Bodra","Orange","Al. Jerozolimskie 160","Warszawa","lukasz.bodra@orange.com")
# add_customer(conn, customers)

select_Where = select_where(conn, "customers", FirstName = "Rafał" )
select_All = select_all(conn, "customers")
print(select_All)

print("")

update(conn, "customers", 1, Email = "rafal.bak@orange.com")
delete_where(conn, "customers", id = 4)
