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
print("connected succesfuly")
while True:
 print("==============================")
 print("EMPLOYEE MANAGEMENT SYSTEM")

 print("==============================")
 print("1. Add Employee")
 print("2. View Employees")
 print("3. Update Employee")
 print("4. Delete Employee")
 print("5. Search Employee")
 print("6. Exit")
 choice=input("Enter your choice:")
 if choice=="1":
    name=input("Enter Employee name: ")
    email=input("Enter Email: ")
    phone=input("Enter phone: ")
    department=input("Enter department: ")
    position=input("Enter position: ")
    salary=input("Enter salary: ")
    sql="INSERT INTO employee(name,email,phone,department,position,salary) VALUES(%s,%s,%s,%s,%s,%s)"
    values=(name,email,phone,department,position,salary)
    mycursor.execute(sql,values)
    mydb.commit()
    print("Employee added successfuly")
 elif choice=="2":
    mycursor.execute("SELECT*FROM employee")
    employees=mycursor.fetchall()
    for employee in employees:
      print(employee)
 elif choice=="3":
   employee_id=input("Enter employee ID to update: ")
   name=input("Enter new name: ")
   email=input("Enter new email: ")
   phone=input("Enter new phone: ")
   department=input("Enter new department: ")
   position=input("Enter new position: ")
   salary=input("Enter new salary: ")
   sql="UPDATE employee SET Name=%s,Email=%s,Phone=%s,Department=%s,Position=%s,Salary=%s WHERE id=%s"
   values=(name,email,phone,department,position,salary,employee_id)
   mycursor.execute(sql,values)
   mydb.commit()
   print("Employee updated successfully!")
 elif choice=="4":
   employee_id=input("Enter employee ID to delete: ")
   sql="DELETE FROM employee WHERE  id=%s"
   mycursor.execute(sql,(employee_id,))
   mydb.commit()
   print("Employee delete succesfully!")
 elif choice =="5":
   employee_id=input("Enter employee ID to serach: ")
   sql="SELECT*FROM employee WHERE id=%s"
   mycursor.execute(sql,(employee_id,))
   employee=mycursor.fetchone()
   if employee:
      print("Employee found")
      print(employee)
   else:
       print("Employee not found")   
 elif choice=="6":
   print("Thank you for using Employee Mnagement System!")
   break  

    