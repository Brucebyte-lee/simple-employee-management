from dotenv import load_dotenv
import os
load_dotenv()
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("DB_PASSWORD"),
    database="employee"
)
mycursor=mydb.cursor()
#print("connected succesfuly")
#mycursor.execute("CREATE DATABASE  IF NOT EXISTS employee")
#print("database created")
mycursor.execute("CREATE TABLE employee(id INT AUTO_INCREMENT PRIMARY KEY,Name VARCHAR(100),Email VARCHAR(100),Phone VARCHAR(100),Department VARCHAR(100),Position VARCHAR(100),Salary VARCHAR(100))")
print("Table successfuly created!")
