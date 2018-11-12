import random

def generate_team_name():
    adjectives = [
        "Giant",
        "Average",
        "Tiny",
        "Magnificent",
        "Marvellous",
        "Crazy",
        "Established",
        "Burbling",
        "Confident",
        "Zimbabwean"
    ]

    nouns = [
        "Cats",
        "Dogs",
        "Bears",
        "Pelicans",
        "CuntSmashers",
        "FixEngines",
        "Tigers",
        "Bananas",
        "Capybaras",
        "Rowans"
    ]

    return "The " + random.choice(adjectives) + " " + random.choice(nouns)
