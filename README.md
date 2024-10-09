# ChefMate

ChefMate is a recipe suggestion chatbot that suggests recipes based on the ingredients provided by the user. It integrates with the [Spoonacular API](https://spoonacular.com/food-api) to fetch recipe suggestions and display detailed recipe information.

## Features

- Users can input a list of ingredients to get recipe suggestions.
- Displays recipe titles, images, and links to detailed recipe instructions.
- Users can view detailed recipes with ingredients, cooking instructions, and preparation time.

## Technologies Used

- Flask (Python web framework)
- HTML, CSS, and JavaScript for the frontend
- Spoonacular API for fetching recipes
- Font Awesome for icons
- Python virtual environment for managing dependencies

## Getting Started

### Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.x
- Virtualenv (optional, but recommended)

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/chefmate.git
   cd chefmate
Create and activate a virtual environment (optional but recommended):

bash
Copier le code
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copier le code
pip install -r requirements.txt
Set up your API key:

Replace the placeholder SPOONACULAR_API_KEY in app.py with your actual Spoonacular API key. You can get one by signing up here.

python
Copier le code
SPOONACULAR_API_KEY = 'your_api_key_here'
Running the Application
Start the Flask application:

bash
Copier le code
flask run
Open your browser and go to http://127.0.0.1:5000/ to interact with the chatbot.

File Structure
php
Copier le code
.
├── app.py               # Main Flask application
├── static/              # Static files (CSS, images, etc.)
├── templates/           # HTML templates for rendering pages
├── venv/                # Python virtual environment (not included in repo)

API Integration
ChefMate uses the Spoonacular API to retrieve recipes. Ensure that you have a valid API key and that it is properly configured in the app.py file. ChefMate interacts with the following API endpoints:

/get_recipes: Fetches recipe suggestions based on ingredients.
/recipe/<recipe_id>: Fetches detailed recipe information for a specific recipe.