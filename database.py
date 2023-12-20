import sqlite3
# Query The DB and Return All Records
def show_all(): 
    conn = sqlite3.connect('customer.db')# Connect to a database 
    c = conn.cursor() # create a cursor
    c.execute("SELECT rowid, * FROM customers") # Query The Database
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit() # Commit command
    conn.close() # Close connection

# Add new record to the table
def add_one(first_name, last_name, email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)", (first_name, last_name, email))
    conn.commit()
    conn.close()

def add_many(list):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?,?,?)", (list))
    conn.commit()
    conn.close()


def delete_one(id):
    conn = sqlite3.connect('customer.db')
    c =conn.cursor()
    c.execute("DELETE from customers WHERE rowid = (?)", id)
    conn.commit()
    conn.close()


# Lookup Where
def name_lookup(first_name):
    conn = sqlite3.connect('customer.db')
    c =conn.cursor()
    c.execute("SELECT * from customers WHERE first_name = (?)", (first_name,))
    items = c.fetchall()
    for item in items:
        print(item)




# Create A Table
# c.execute("""CREATE TABLE customers (
#           first_name text,
#           last_name text,
#           email text
#     )""")

# Datatypes
# NULL
# INTEGER
# REAL
# TEXT
# BLOB

# c.execute("INSERT INTO customers VALUES ('Brysl', 'Ltd', 'brysol@gmail.com')")

# many_customers = [
#     ('Briana', 'Ondiso', 'brian@gmail.com'), 
#     ('ShotoK', 'Todoroski', 'Shoto@gmail.com'), 
#     ('Brysolutions', 'PLC', 'Brysl@gmail.com')
#     ]

# c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

# Query and Fetch
# c.execute("SELECT rowid, * FROM customers")
# # c.fetchone()
# # c.fetchmany()
# items = c.fetchall()

# for item in items:
#     print(item[0]+ " " + item[1] + " \t "+ item[2])

# Update Records
# c.execute("""UPDATE customers SET email = 'bry@gma.com'
#           WHERE rowid = 3
# """)

# Delete a Record

# c.execute("DELETE from customers WHERE rowid = 6")


# Ordering

# c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC ")
# conn.commit()

# QUERY THE DB
# WHERE CLAUSE
# c.execute("SELECT  * FROM customers WHERE first_name LIKE 'Br%' ")
# conn.commit()
    
# Query The Database - AND/OR

# c.execute("SELECT rowid, * FROM customers WHERE first_name LIKE 'Sho%' AND rowid = 5")
# conn.commit()
# c.execute("SELECT rowid, * FROM customers WHERE first_name LIKE 'Sho%' OR rowid = 1")
# conn.commit()
# c.execute("SELECT rowid, * FROM customers WHERE first_name LIKE 'Sho%' OR rowid = 5 OR last_name LIKE '%__so'")
# conn.commit()

# Limiting Reuslts
# c.execute("SELECT rowid, * FROM customers LIMIT 2")
# conn.commit()

# Drop A Table
# c.execute("DROP TABLE customers")
# conn.commit()

#Commit command
# conn.commit()
# Close oconnection
# conn.close()