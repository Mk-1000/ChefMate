import spacy
from spellchecker import SpellChecker
from nltk.corpus import wordnet as wn
import re
from spacy.matcher import PhraseMatcher

nlp = spacy.load('en_core_web_trf')
spell = SpellChecker()

matcher = PhraseMatcher(nlp.vocab)

common_ingredients = [text.lower() for text in [
    "Carrot", "Cucumber", "Potato", "Spinach", "Broccoli", "Egg", "Eggs", "Beef", "Pork",
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
    "White Sugar", "Flour", "Baking Powder", "Baking Soda", "Yeast", "Cocoa Powder"
]]

common_ingredients_patterns = [nlp(text) for text in common_ingredients]
matcher.add("FOOD", None, *common_ingredients_patterns)

def correct_spelling(text):
    corrected = [spell.correction(word) for word in text.split()]
    return ' '.join(corrected)

def get_synonyms(word):
    synonyms = set()
    for synset in wn.synsets(word):
        for lemma in synset.lemmas():
            synonyms.add(lemma.name())
    return synonyms

def extract_quantities(text):
    pattern = r'(\d+\s?(?:cups?|tsp|tbsp|grams?|kg|liters?|ml|ounces?|oz|pounds?|lbs?))\s(.+)'
    matches = re.findall(pattern, text)
    return matches

def extract_custom_ingredients(doc):
    matches = matcher(doc)
    return [doc[start:end].text for match_id, start, end in matches]

def extract_ingredients(nlp_text):
    """ Enhanced ingredient extraction. """
    corrected_text = correct_spelling(nlp_text).lower()
    print("Corrected Text:", corrected_text)

    doc = nlp(corrected_text)
    
    # Extract ingredients from NER and PhraseMatcher
    ingredients = [ent.text for ent in doc.ents if ent.label_ == 'FOOD']
    ingredients += extract_custom_ingredients(doc)

    if not ingredients:
        ingredients = [token.text for token in doc if token.pos_ == 'NOUN' and token.is_alpha]

    # Add synonyms for recognized ingredients
    all_ingredients = ingredients[:]
    for item in ingredients:
        all_ingredients += get_synonyms(item)

    # Extract quantities and add them to the ingredients list
    quantities = extract_quantities(corrected_text)
    ingredients_with_quantities = [f'{quantity} of {ingredient}' for quantity, ingredient in quantities]
    
    # Merge all extracted ingredients and remove duplicates
    all_ingredients += ingredients_with_quantities
    all_ingredients = list(set(all_ingredients))

    return ', '.join(all_ingredients)

# Example usage
# input_text = "I need 2 Eggs and some spinach."
# result = extract_ingredients(input_text)
# print(result)
