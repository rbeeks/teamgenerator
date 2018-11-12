import random

def generate_team_name():
    adjectives = [
        "Giant",
        "Average",
        "Tiny"
    ]

    nouns = [
        "Cats",
        "Dogs",
        "Bears",
        "Pelicans"
    ]

    return "The " + random.choice(adjectives) + " " + random.choice(nouns)
