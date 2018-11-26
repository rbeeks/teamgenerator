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
        "Zimbabwean",
        "Ingolrious",
        "Ravishing",
        "Indubious",
        "Dubious",
        "Realistic",
        "Unrealistic",
        "Loquacious",
        "Luminous",
        "Sclerotic",
        "Withering",
        "Feckless",
        "Boorish",
        "Hysterical",
        "Pickled",
        "Gaping",
        "Cyborg",
        "Toasted"
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
        "Rowans",
        "FartBlasters",
        "PicklePickers",
        "PeckerHandlers",
        "Rats",
        "Hullaballoos",
        "Wippersnappers",
        "Poppycocks",
        "Otters",
        "FartSplitters",
        "PoopCollectors",
        "Mormons",
        "Antelopes",
        "Beekmeyers",
        "Plumbers",
        "Pirates
    ]

    return "The " + random.choice(adjectives) + " " + random.choice(nouns)
