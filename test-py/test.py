import mysql.connector



mydb = mysql.connector.connect(
  host="localhost",
  user="test",
  password="P@ssw0rdf0rf#n"
)

print(mydb) 

print("----------------------------------")

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM test.users")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

print("----------------------------------")

mycursor.execute("SELECT * FROM test.recipes")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
#print("hello world")