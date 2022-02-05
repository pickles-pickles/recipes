from msilib.schema import Class
import mysql.connector
from password import db_password

#connect to db

mydb = mysql.connector.connect(
  host="localhost",
  user="test",
  password=db_password
)
mycursor = mydb.cursor()


""" OBJECT ORIENTD PROGRAMMING STUFF """

#define class

class Recipe:
    def __init__(self, name, description, img_url, difficulty, category):
        self.name = name
        self.description = description
        self.img_url = img_url
        self.difficulty = difficulty
        self.category = category
        
    #selectRecipes in bound to class, not instance
    @classmethod
    def selectRecipes(self):
        mycursor.execute("SELECT idrecipes, recipename, recipe_description, recipe_img, recipedifficulty, category  , cat_name FROM test.recipes INNER JOIN test.categories ON test.recipes.category=test.categories.idcategories;")
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

    def readRecipe(self):
        sql = """ SELECT FROM test.recipes  WHERE recipename = %s """ 
        mycursor.execute(sql, (self.name, ))
        mydb.commit()
        print(mycursor.rowcount, "record selected.")  

""" INGREDIENTS """

class Ingredient:
    def __init__(self, ing_name):
        self.ing_name = ing_name

    @classmethod
    def selectIngredients(self):
        mycursor.execute("SELECT ingredient_name FROM test.ingredients ")
        myresult = mycursor.fetchall()
        return myresult
    """ SELECT ingredient_name FROM test.ingredients INNER JOIN test.recipes ON test.ingredients.idrecipes_2 =test.recipes.idrecipes; """

    @classmethod
    def selectIngredients2(self):
        mycursor.execute("")
        myresult = mycursor.fetchall()
        return myresult

    def createIngredient(self):
        sql = "INSERT INTO test.ingredients ( ingredient_name ) VALUES (%s)"
        mycursor.execute(sql, (self.ing_name, ))
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
    
def selectRecipeIngredients():
    mycursor.execute("""SELECT recipes.idrecipes, recipes.recipename, ingredients.ingredient_name
    FROM test.recipes
    JOIN 
    test.recipe_has_ingredients
    ON
    test.recipes.idrecipes = test.recipe_has_ingredients.recipe
    JOIN 
    test.ingredients
    ON
    test.ingredients.idingredients = test.recipe_has_ingredients.ingredient
     """)
    myresult = mycursor.fetchall()
    return myresult

""" STUFF FROM BELOW HERE IS TO BE USED ONLY IF WE HAVE TIME TO MAKE SOME EXTRAS FOR THE PROEJCT """
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