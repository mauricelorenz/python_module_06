def validate_ingredients(ingredients: str) -> str:
    valid = ["fire", "water", "earth", "air"]
    for item in valid:
        if item in ingredients:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
