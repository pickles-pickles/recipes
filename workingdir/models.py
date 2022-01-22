from msilib.schema import Class
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

def updateRecipe(name, category):
    sql_update_query = """UPDATE test.recipes SET recipecategory = %s WHERE recipename = %s"""
    input_data = (category,name )
    mycursor.execute(sql_update_query, input_data)
    mydb.commit()
    print(mycursor.rowcount,"record updated successfully ")

updateRecipe("fench fries", "potatoes")

def deleteRecipe(name):
    sql = """ DELETE FROM test.recipes  WHERE recipename = %s """ 
    mycursor.execute(sql, (name,))
    mydb.commit()
    print(mycursor.rowcount, "record deleted.")

deleteRecipe("chocolate cake")
""" createRecipe("a", "a") """

""" OBJECT ORIENTD PROGRAMMING STUFF """

class Recipe:
    def __init__(self, name, category, difficulty):
        self.name = name
        self.category = category
        self.difficulty = difficulty

    
    def selectRecipes(self):
        mycursor.execute("SELECT * FROM test.recipes")
        myresult = mycursor.fetchall()
        return myresult
    
    def createRecipe(self):
        sql = "INSERT INTO test.recipes (recipename, recipecategory) VALUES (%s, %s)"
        mycursor.execute(sql, (self.name, self.category))
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")

    def updateRecipe(self):
        sql_update_query = """UPDATE test.recipes SET recipecategory = %s WHERE recipename = %s"""
        input_data = (self.category,self.name )
        mycursor.execute(sql_update_query, input_data)
        mydb.commit()
        print(mycursor.rowcount,"record updated successfully ")

    def deleteRecipe(self):
        sql = """ DELETE FROM test.recipes  WHERE recipename = %s """ 
        mycursor.execute(sql, (self.name,))
        mydb.commit()
        print(mycursor.rowcount, "record deleted.")