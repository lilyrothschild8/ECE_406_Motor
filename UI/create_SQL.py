import sqlite3

connection = sqlite3.connect("Ford_Data.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE Employee (User_Name TEXT, Pass_Word TEXT, Access_Code INTEGER, Clearance INTEGER)")
cursor.execute("INSERT INTO Employee VALUES ('Test', 'Dummy', 016104662, 2)")
rows = cursor.execute("SELECT User_Name, Pass_Word, Access_Code, Clearance FROM Employee").fetchall()
print(rows)
connection.commit()
connection.close()