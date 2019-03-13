import sqlite3, os

DBFILENAME = os.path.join(os.path.dirname(__file__), 'bank.db')

flushing = [("Lockett", "Walker", "S000000001", 45000, 1), ("Coleman", "Casey", "S000000002", 70000, 1), ("Kilome", "Franklyn", "S000000003", 67000, 1), ("Santiago", "Hecton", "S000000004", 100000, 1)]

houston = [("Valdez", "Framber", "S000000005", 39000, 2), ("Peacock", "Brad", "S000000006", 51000, 2), ("Guduan", "Reymin", "S000000007", 67000, 2), ("Cole", "Gerrit", "S000000008", 55000, 2)]

with sqlite3.connect(DBFILENAME) as conn:
    cur = conn.cursor()

    SQL="""INSERT INTO branch (City, State, Zip) 
    VALUES ('Flushing','NY', 11368)
    """        
    cur.execute(SQL)

    SQL="""INSERT INTO branch (City, State, Zip) 
    VALUES ('Houston','TX', 77002)
    """        
    cur.execute(SQL)

    SQL="""INSERT INTO employee (LastName, FirstName, EmployeeID, Salary, branchpk) 
    VALUES (?, ?, ?, ?, ?)"""

    for i in flushing:    
        cur.execute(SQL, i)
    
    for j in houston:
        cur.execute(SQL, j)
    
# Write a SQL UPDATE statement to change Reymin Guduan's salary to 73000

    SQL = """UPDATE employee SET Salary = 73000 WHERE FirstName = 'Reymin'"""
    cur.execute(SQL)

# Write a SQL SELECT statement to select all employees in New York that make over 70000 a year

    SQL="""SELECT * FROM employee WHERE Salary > 70000 AND branchpk = 1"""

    cur.execute(SQL)
    result = cur.fetchall()
    print(result)