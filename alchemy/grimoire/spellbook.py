def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients
    validation = validate_ingredients(ingredients)
    message = "Spell rejected" if "INVALID" in validation else "Spell recorded"
    return f"{message}: {spell_name} ({validation})"
