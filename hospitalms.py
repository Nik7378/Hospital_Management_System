import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="hospital"
)

mycursor = mydb.cursor()

def addpatient():
  mycursor.execute("CREATE TABLE if not exists patients (id INT AUTO_INCREMENT PRIMARY KEY, name text, age int, mobile bigint, address text, blood_group text, gender text, dob date);")
  print("-----------------------------------------------------------------")
  print("                      Add Patient Record                         ")
  print("-----------------------------------------------------------------")
  name = input("Name: ")
  age = int(input("Age: "))
  mobile = int(input("Mobile.No: "))
  address = input("Address: ")
  blood_group = input("Blood Group: ")
  gender = input("Gender(M/F): ")
  dob = input("Date of birth(yyyy-mm-dd): ")
  query = "insert into patients (name, age, mobile, address, blood_group, gender, dob) values(%s,%s,%s,%s,%s,%s,%s)"
  val = (name, age, mobile, address, blood_group, gender, dob)
  mycursor.execute(query, val)
  print("-----------------------------------------------------------------")
  print("Patient Record Added")
  mydb.commit()
  viewpatient()

def editpatient():
  print("-----------------------------------------------------------------")
  print("                    Update Patient Record                        ")
  print("-----------------------------------------------------------------")      
  id = int(input("Enter id of Patient you want to update: "))
  mobile = int(input("Enter updated mobile no: "))
  query = "update patients set mobile = %s where id = %s"
  val = (mobile, id,)
  mycursor.execute(query, val)
  print("-----------------------------------------------------------------")
  print("Patient Details Updated")
  mydb.commit()
  viewpatient()


def delpatient():
  print("-----------------------------------------------------------------")
  print("                      Delete Patient Record                        ")
  print("-----------------------------------------------------------------")  
  id = int(input("Enter id of Patient you want to delete: "))
  query = "delete from patients where id = %s"
  val = (id,)
  mycursor.execute(query, val)
  print("-----------------------------------------------------------------")
  print("Patient Record Deleted")
  mydb.commit()
  viewpatient()

def viewpatient():
  print("-----------------------------------------------------------------")
  print("                   View Patients Records                         ")
  print("-----------------------------------------------------------------")
  mycursor.execute("select * from patients;")
  res = mycursor.fetchall()
  for i in res:
    print("ID : ", i[0])
    print("Name : ", i[1])
    print("Age : ", i[2])
    print("Mobile : ", i[3])
    print("Address : ", i[4])
    print("Blood Group : ", i[5])
    print("Gender : ", i[6])
    print("Date of birth : ", i[7])
    print("-----------------------------------------------------------------")

def adddoctor():
  mycursor.execute("CREATE TABLE if not exists doctors (id INT AUTO_INCREMENT PRIMARY KEY, name text, dept text, qualification text, mobile bigint, address text, gender text);")
  
  print("-----------------------------------------------------------------")
  print("                      Add Doctor Record                          ")
  print("-----------------------------------------------------------------")

  name = input("Name: ")
  dept = input("Dept: ")
  qualification = input("Qualification: ")
  mobile = int(input("Mobile.No: "))
  address = input("Address: ")
  gender = input("Gender(M/F): ")

  query = "insert into doctors (name, dept, qualification, mobile, address, gender) values(%s,%s,%s,%s,%s,%s)"
  val = (name, dept, qualification, mobile, address, gender)
  mycursor.execute(query, val)
  print("-----------------------------------------------------------------")
  print("Doctor Record Added")
  mydb.commit()
  viewdoctor()

def editdoctor():
  print("-----------------------------------------------------------------")
  print("                    Update Doctor Record                         ")
  print("-----------------------------------------------------------------")      
  id = int(input("Enter id of Doctor you want to update: "))
  mobile = int(input("Enter updated mobile no: "))
  query = "update doctors set mobile = %s where id = %s"
  val = (mobile, id,)
  mycursor.execute(query, val)
  print("-----------------------------------------------------------------")
  print("Doctor Record Updated")
  mydb.commit()
  viewdoctor()

def deldoctor():
  print("-----------------------------------------------------------------")
  print("                      Delete Doctor Record                        ")
  print("-----------------------------------------------------------------")  
  id = int(input("Enter id of Doctor you want to delete: "))
  query = "delete from doctors where id = %s"
  val = (id,)
  mycursor.execute(query, val)
  print("-----------------------------------------------------------------")
  print("Doctor Record Deleted")
  mydb.commit()
  viewdoctor()

def viewdoctor():
  print("-----------------------------------------------------------------")
  print("                   View Doctors Records                          ")
  print("-----------------------------------------------------------------")
  mycursor.execute("select * from doctors;")
  res = mycursor.fetchall()
  for i in res:
    print("ID : ", i[0])
    print("Name : ", i[1])
    print("Dept : ", i[2])
    print("Qualification : ", i[3])
    print("Mobile : ", i[4])
    print("Address : ", i[5])
    print("Gender : ", i[6])
    print("-----------------------------------------------------------------")

while True:
  print("-----------------------------------------------------------------")
  print("            Welcome to Hospital Management System                ")
  print("-----------------------------------------------------------------")
  print("1. To manage patients menu.\n2. To manage doctors menu\n3. Exit")
  print("-----------------------------------------------------------------")
  ch = int(input("Enter your choice: "))
  print("-----------------------------------------------------------------")
  
  if ch == 1:
    while True:
      print("-----------------------------------------------------------------")
      print("                        Manage Patients                          ")
      print("-----------------------------------------------------------------")
      print("1. Add Patient Details\n2. Update Patient Details\n3. Delete Patient Details\n4. View All Patients Details\n5. Exit")
      print("-----------------------------------------------------------------")
      ch = int(input("Enter your choice: "))
      print("-----------------------------------------------------------------")
      
      if ch == 1:
          addpatient()
      elif ch == 2:
          editpatient()
      elif ch == 3:
          delpatient()
      elif ch == 4:
          viewpatient()
      elif ch == 5:
          print("Thank You For Visiting Us!")
          break
      else:
          print("Wrong Choice")

  elif ch == 2:
    while True:
      print("-----------------------------------------------------------------")
      print("                        Manage Doctors                          ")
      print("-----------------------------------------------------------------")
      print("1. Add Doctor Details\n2. Update Doctor Details\n3. Delete Doctor Details\n4. View All Doctors Details\n5. Exit")
      print("-----------------------------------------------------------------")
      ch = int(input("Enter your choice: "))
      print("-----------------------------------------------------------------")
      
      if ch == 1:
          adddoctor()
      elif ch == 2:
          editdoctor()
      elif ch == 3:
          deldoctor()
      elif ch == 4:
          viewdoctor()
      elif ch == 5:
          print("Thank You For Visiting Us!")
          break
      else:
          print("Wrong Choice")
          
  elif ch == 3:
          print("Thank You For Visiting Us!")
          break        
  else:
          print("Wrong Choice")




