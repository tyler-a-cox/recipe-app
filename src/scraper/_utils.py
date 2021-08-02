import django
import re

UNITS = ["CUP", "PINCH", "OUNCE", "POUND", "TEASPOON",
         "TABLESPOON", "OZ", "TBSP", "TSP", "LB"]


ABBREVIATION = {
    "OZ": "OUNCE",
    "TBSP": "TABLESPOON",
    "TSP": "TEASPOON",
    "LB": "POUND",
}

def parse_ingredient(ingredient):
    """
    """
    matches = []
    for unit in UNITS:
        match = re.search(unit, ingredient.text, re.IGNORECASE)
        if match:
            matched = ABBREVIATION.get(match.group(), match.group())
            matches.append(matched)

    return matches
