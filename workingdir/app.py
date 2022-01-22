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
        createRecipe(name, category)
    
    recipes = selectRecipes()

    return render_template('index.html', recipes = recipes)

if __name__ == "__main__":
    app.run(debug=True)
