import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="test",
  password="P@ssw0rdf0rf#n"
)

print(mydb) 

print("----------------------------------")

mycursor = mydb.cursor()

def selectUsers():
    mycursor.execute("SELECT * FROM test.users")
    myresult = mycursor.fetchall()
    return myresult
"""     for x in myresult:
        print(x)

selectUsers()
print("----------------------------------") """

def selectRecipes():
    mycursor.execute("SELECT * FROM test.recipes")
    myresult = mycursor.fetchall()
    """ for x in myresult:
        print(x) """
    # you can use return instead of a loop
    return myresult



def createRecipe(name, category):
    sql = "INSERT INTO test.recipes (recipename, recipecategory) VALUES (%s, %s)"
    
    mycursor.execute(sql, (name, category))
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

def deleteRecipe(name):
    sql = "DELETE FROM test.recipes  WHERE recipename = 'chocolate cake' "
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record deleted.")

deleteRecipe("chocolate cake")
""" createRecipe("a", "a") """
