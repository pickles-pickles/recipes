from distutils.log import debug
""" from nis import cat
from pydoc import stripid """
from flask import Flask, render_template, request
from flask_cors import CORS
from models import *

app = Flask(__name__)

CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        pass

    if request.method == 'POST':
        name = request.form.get('name')
        category = request.form.get('category')
        difficulty = request.form.get('difficulty')
        global newRecipe
        newRecipe = Recipe(name, category, difficulty)
        newRecipe.createRecipe()
    
    recipes = Recipe.selectRecipes()
    ingredients= Ingredient.selectIngredients()
    """ users = selectUsers() """

    return render_template('index.html', recipes = recipes, ingredients = ingredients )

@app.route('/food.html')
def food():
    recipes = Recipe.selectRecipes()
    return render_template('food.html', recipes = recipes,)  

@app.route('/category.html')
def category():
    categories = Category.selectCategories()
    return render_template('category.html', categories = categories )

@app.route('/user.html')
def user():
    
    return render_template('user.html', )



@app.route('/add-recipe.html', methods=['GET', 'POST'])
def add_recipe():
    if request.method == "GET":
        pass

    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        img_url = request.form.get('img_url')
        difficulty = request.form.get('difficulty')
        category = request.form.get('category')
        global newRecipe
        newRecipe = Recipe(name, description, img_url, difficulty, category)
        newRecipe.createRecipe()
        #ingredient
        
        ingredient = request.form.get("ing")
        newIngredient = Ingredient(ingredient)
        newIngredient.createIngredient()
    
    recipes = Recipe.selectRecipes()
    categories = Category.selectCategories()
    ingredients = Ingredient.selectIngredients()
    ingredients2 = Ingredient.selectIngredients2()
    
    return render_template('/food/add-recipe.html', recipes = recipes, categories=categories, ingredients = ingredients, ingredients2 = ingredients2)


@app.route('/delete-recipe.html', methods=['GET', 'POST'])
def delete_recipe():
    if request.method == "GET":
        pass

    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        img_url = request.form.get('img_url')
        difficulty = request.form.get('difficulty')
        category = request.form.get('category')

        global toDelete
        toDelete = Recipe(name, description, img_url, difficulty, category)
        toDelete.deleteRecipe()

    recipes = Recipe.selectRecipes()

    return render_template('/food/delete-recipe.html', recipes = recipes )


@app.route('/update-recipe.html', methods=['GET', 'POST'])
def update_recipe():
    if request.method == "GET":
        pass

    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        img_url = request.form.get('img_url')
        difficulty = request.form.get('difficulty')
        category = request.form.get('category')

        global toUpdate
        toUpdate = Recipe(name, description, img_url, difficulty, category)
        toUpdate.updateRecipe()

    recipes = Recipe.selectRecipes()
    categories = Category.selectCategories()

    return render_template('/food/update-recipe.html', recipes = recipes, categories = categories )

#############################################################################################
                                        ## WORKING HERE ##
#############################################################################################

@app.route("/read-recipe.html", methods=["GET"])
def readRecipe():
    if request.method== "GET":
        recipes = Recipe.selectRecipes()
        idrecipes = request.args.get('idrecipes')
        recipeing = selectRecipeIngredients()
    return render_template("/food/read-recipe.html", recipes = recipes, idrecipes = idrecipes, recipeing = recipeing)

#######################################################################################

""" category """

@app.route('/add-category.html', methods=['GET', 'POST'])
def add_category():
    if request.method == "GET":
        pass

    if request.method == 'POST':
        cat_name = request.form.get('cat_name')
        img_url = request.form.get('img_url')
        featured = request.form.get('featured')
        active = request.form.get('active')
        global newCategory
        newCategory = Category(cat_name, img_url, featured, active)
        newCategory.createCategory()
        #createRecipe(name, category)
    
    categories = Category.selectCategories()
    

    return render_template('/category/add-category.html', categories = categories, )

""" 
Always keep this if statement in the bottom
 """
if __name__ == "__main__":
    app.run(debug=True)


""" recipe = request.form.get('recipe')
        #global recipeToDelete
        #recipe = recipe.strip("()")
        #recipeToDelete = Recipe(recipe[0], recipe[1], recipe[2], recipe[3], recipe[4])
        #print(recipeToDelete)
        #recipeToDelete.deleteRecipe()
        Recipe.deleteRecipe() """