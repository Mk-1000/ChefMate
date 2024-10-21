# ChefMate

ChefMate is a recipe recommendation application that leverages natural language processing (NLP) techniques to extract ingredients from user input and suggest recipes based on those ingredients. The application aims to provide an intuitive and user-friendly interface for cooking enthusiasts, making it easy to find recipes tailored to available ingredients.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- **Ingredient Extraction**: Parses user input to identify and extract ingredient names using Named Entity Recognition (NER).
- **Spell Checking and Correction**: Corrects typos and misspellings in user input to enhance accuracy in recipe suggestions.
- **Synonym Recognition**: Utilizes WordNet to recognize synonyms and variations of ingredient names, increasing flexibility.
- **Contextual Understanding**: Implements advanced transformer models to understand the context of ingredients within complex sentences.
- **Phrase Matching**: Recognizes common phrases associated with ingredient lists for better extraction.

## Technologies Used

- **Flask**: A lightweight web framework for Python.
- **spaCy**: A library for advanced natural language processing.
- **NLTK**: The Natural Language Toolkit for handling linguistic data.
- **Requests**: A simple HTTP library for Python to make API calls.
- **WordNet**: A lexical database for the English language.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Mk-1000/ChefMate.git
   cd ChefMate
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask application:
   ```bash
   flask run
   ```

2. Access the application in your web browser at:
   ```
   http://127.0.0.1:5000
   ```
