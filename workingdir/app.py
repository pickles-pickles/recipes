from distutils.log import debug
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
        #createRecipe(name, category)
    
    recipes = Recipe.selectRecipes()
    """ users = selectUsers() """

    return render_template('index.html', recipes = recipes, )

""" if __name__ == "__main__":
    app.run(debug=True) """

@app.route('/food.html')
def food():
    foods = Recipe.selectRecipes()
    return render_template('food.html', foods = foods,)  

@app.route('/category.html')
def category():
    
    return render_template('category.html', )

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
        #createRecipe(name, category)
    
    recipes = Recipe.selectRecipes()
    

    return render_template('/food/add-recipe.html', recipes = recipes, )

""" 
Always keep this if statement in the bottom
 """
if __name__ == "__main__":
    app.run(debug=True)