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
    
    recipes = newRecipe.selectRecipes()
    users = selectUsers()

    return render_template('index.html', recipes = recipes, users = users)

if __name__ == "__main__":
    app.run(debug=True)
