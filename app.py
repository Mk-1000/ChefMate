from flask import Flask, render_template, request, jsonify
import requests
from nlp_utils import extract_ingredients

app = Flask(__name__)

# Replace with your Spoonacular API key
SPOONACULAR_API_KEY = 'Your-Spoonacular-API-key'
SPOONACULAR_BASE_URL = 'https://api.spoonacular.com/recipes/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_recipes', methods=['POST'])
def get_recipes():
    data = request.get_json()  # Get JSON data
    user_input = data.get('ingredients', '')

    # Ensure that ingredients are provided
    if not user_input:
        return jsonify({'error': 'Please enter some ingredients'})

    # Extract ingredients from natural language input
    ingredients = extract_ingredients(user_input)

    if not ingredients:
        return jsonify({'error': 'No valid ingredients detected. Please check your spelling or try different ingredients.'})

    # Fetch recipes using the Spoonacular API
    response = requests.get(
        f'{SPOONACULAR_BASE_URL}findByIngredients',
        params={'ingredients': ingredients, 'apiKey': SPOONACULAR_API_KEY}
    )

    if response.status_code == 200:
        recipes = response.json()
        if not recipes:
            return jsonify({'error': 'No recipes found for the given ingredients.'})

        recipe_suggestions = [{
            'title': recipe['title'],
            'id': recipe['id'],
            'image': recipe['image']
        } for recipe in recipes]

        return jsonify(recipe_suggestions)
    else:
        return jsonify({'error': 'Unable to fetch recipes, please try again later.'})


@app.route('/recipe/<int:recipe_id>', methods=['GET'])
def get_recipe_details(recipe_id):
    # Fetch detailed recipe information using the Spoonacular API
    response = requests.get(
        f'{SPOONACULAR_BASE_URL}{recipe_id}/information',
        params={'apiKey': SPOONACULAR_API_KEY}
    )

    if response.status_code == 200:
        recipe_details = response.json()
        return render_template('recipe_details.html', recipe=recipe_details)
    else:
        return "Recipe details not available at the moment.", 404


if __name__ == '__main__':
    app.run(debug=True)
