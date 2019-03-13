import sqlite3, os

def create_schema(filename):
    dbfilename = os.path.join(os.path.dirname(__file__), filename)
    conn = sqlite3.connect(dbfilename)
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS branch (
        branchpk INTEGER PRIMARY KEY AUTOINCREMENT,
        City VARCHAR(128),
        State VARCHAR(2),
        Zip INTEGER
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS employee (
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        LastName VARCHAR(128),
        FirstName VARCHAR(128),
        EmployeeID INTEGER,
        Salary VARCHAR(128),
        branchpk INTEGER,
        FOREIGN KEY(branchpk) REFERENCES branch(branchpk)
    )""")

    
    c.close()

create_schema('bank.db')