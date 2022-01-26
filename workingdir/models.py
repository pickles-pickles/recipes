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



def deleteRecipe(name):
    sql = """ DELETE FROM test.recipes  WHERE recipename = %s """ 
    mycursor.execute(sql, (name,))
    mydb.commit()
    print(mycursor.rowcount, "record deleted.")

deleteRecipe("chocolate cake")
""" createRecipe("a", "a") """

""" OBJECT ORIENTD PROGRAMMING STUFF """

class Recipe:
    def __init__(self, name, description, img_url, difficulty, category):
        self.name = name
        self.description = description
        self.img_url = img_url
        self.difficulty = difficulty
        self.category = category
        

    @classmethod
    def selectRecipes(self):
        mycursor.execute("SELECT recipename, recipe_description, recipe_img, recipedifficulty, category  , cat_name FROM test.recipes INNER JOIN test.categories ON test.recipes.category=test.categories.idcategories;")
        myresult = mycursor.fetchall()
        return myresult
    
    def createRecipe(self):
        sql = "INSERT INTO test.recipes (recipename, recipe_description, recipe_img, recipedifficulty, category) VALUES (%s, %s, %s, %s, %s)"
        mycursor.execute(sql, (self.name, self.description, self.img_url, self.difficulty, self.category))
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")

    def updateRecipe(self):
        sql_update_query = """UPDATE test.recipes SET recipename = %s, recipe_description= %s, recipe_img = %s, recipedifficulty = %s,  category = %s WHERE recipename = %s"""
        input_data = (self.name, self.description, self.img_url, self.difficulty, self.category, self.name )
        mycursor.execute(sql_update_query, input_data)
        mydb.commit()
        print(mycursor.rowcount,"record updated successfully ")
        
    
    def deleteRecipe(self):
        sql = """ DELETE FROM test.recipes  WHERE recipename = %s """ 
        mycursor.execute(sql, (self.name, ))
        mydb.commit()
        print(mycursor.rowcount, "record deleted.")
        """  mycursor.execute(sql, (self.name, self.description, self.img_url, self.difficulty, self.category)) """
       

""" CATEGORIES """

class Category(Recipe):
    def __init__(self, cat_name, img_url, featured, active):
        self.cat_name = cat_name
        self.img_url = img_url
        self.featured = featured
        self.active = active

    def createCategory(self):
        sql = "INSERT INTO test.categories (cat_name, cat_img, cat_featured, cat_active) VALUES (%s, %s, %s, %s)"
        mycursor.execute(sql, (self.cat_name, self.img_url, self.featured, self.active))
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")

    @classmethod
    def selectCategories(self):
        mycursor.execute("SELECT * FROM test.categories")
        myresult = mycursor.fetchall()
        return myresult