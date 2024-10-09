from flask import Flask, render_template, request, jsonify
import requests
import spacy

app = Flask(__name__)

# Load the spaCy model for NLP
nlp = spacy.load('en_core_web_sm')

# Replace with your Spoonacular API key
SPOONACULAR_API_KEY = 'your_api_key_here'
SPOONACULAR_BASE_URL = 'https://api.spoonacular.com/recipes/'

@app.route('/')
def index():
    return render_template('index.html')

def extract_ingredients(nlp_text):
    """ Extracts potential ingredient words using spaCy's named entity recognition (NER) and part-of-speech tagging. """
    doc = nlp(nlp_text)
    ingredients = []

    # Loop through the entities in the document and extract food-related entities
    for ent in doc.ents:
        if ent.label_ == 'FOOD':
            ingredients.append(ent.text)

    # If no food-related entities found, fall back to nouns (could also be ingredients)
    if not ingredients:
        ingredients = [token.text for token in doc if token.pos_ == 'NOUN' and token.is_alpha]

    # Check if the input text contains common ingredients not detected by NER
    common_ingredients = [            "Carrot", "Cucumber", "Potato", "Spinach", "Broccoli", "Egg", "Beef", "Pork",
            "Lemon", "Avocado", "Tomato", "Onion", "Garlic", "Cheese", "Pepper", "Chicken",
            "Basil", "Mushrooms", "Rice", "Quinoa", "Pasta", "Zucchini", "Bell Pepper",
            "Lettuce", "Cauliflower", "Eggplant", "Sweet Potato", "Pumpkin", "Radish",
            "Green Beans", "Asparagus", "Peas", "Kale", "Cabbage", "Chickpeas", "Lentils",
            "Tofu", "Salmon", "Shrimp", "Turkey", "Sausage", "Pineapple", "Strawberries",
            "Blueberries", "Banana", "Peach", "Mango", "Kiwi", "Orange", "Grapes", "Raspberry",
            "Blackberry", "Coconut", "Almond", "Walnut", "Hazelnut", "Pistachio", "Peanut",
            "Soy Sauce", "Olive Oil", "Vinegar", "Honey", "Mustard", "Ketchup", "Mayonnaise",
            "Chili Powder", "Cinnamon", "Oregano", "Thyme", "Rosemary", "Parsley", "Cilantro",
            "Ginger", "Turmeric", "Paprika", "Nutmeg", "Cardamom", "Vanilla", "Brown Sugar",
            "White Sugar", "Flour", "Baking Powder", "Baking Soda", "Yeast", "Cocoa Powder"]  # Added 'Banana'
    for item in common_ingredients:
        if item.lower() in nlp_text.lower() and item not in ingredients:
            ingredients.append(item)

    # Log the raw input and extracted ingredients for debugging
    print(f"Raw input: {nlp_text}")
    print(f"Extracted ingredients before deduplication: {ingredients}")

    # Remove duplicates
    ingredients = list(set(ingredients))

    return ','.join(ingredients)


@app.route('/get_recipes', methods=['POST'])
def get_recipes():
    data = request.get_json()  # Get JSON data
    user_input = data.get('ingredients', '')

    # Ensure that ingredients are provided
    if not user_input:
        return jsonify({'error': 'Please enter some ingredients'})

    # Extract ingredients from natural language input
    ingredients = extract_ingredients(user_input)

    # Log extracted ingredients for debugging
    # print(f"Extracted ingredients: {ingredients}")

    # Check if any ingredients were extracted
    if not ingredients:
        return jsonify({'error': 'Unable to extract ingredients. Please try again with different phrasing.'})

    # Fetch recipes using the Spoonacular API
    response = requests.get(
        f'{SPOONACULAR_BASE_URL}findByIngredients',
        params={'ingredients': ingredients, 'apiKey': SPOONACULAR_API_KEY}
    )

    # Log the API response for debugging
    # print(f"API Response: {response.status_code} - {response.text}")

    if response.status_code == 200:
        recipes = response.json()
        recipe_suggestions = []

        for recipe in recipes:
            recipe_suggestions.append({
                'title': recipe['title'],
                'id': recipe['id'],
                'image': recipe['image']
            })

        if not recipe_suggestions:
            return jsonify({'error': 'No recipes found for the given ingredients.'})

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
