import random

def generate_team_name():
    adjectives = [
        "Giant",
        "Average",
        "Tiny",
        "Magnificent",
        "Marvellous",
        "Crazy",
        "Established"
    ]

    nouns = [
        "Cats",
        "Dogs",
        "Bears",
        "Pelicans",
        "CuntSmashers",
        "FixEngines",
        "Tigers"
    ]

    return "The " + random.choice(adjectives) + " " + random.choice(nouns)
