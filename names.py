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
        "Inglorious",
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
        "Pointless",
        "Hilarious",
        "Dystopian",
        "Angelic",
        "Telegraphic",
        "Fat",
        "KFC Loving",
        "Swashbuckling",
        "Xenophilic",
        "Football Playing",
        "Romantic",
        "Convex",
        "Mineral Rich",
        "0 Indexed",
        "Magisterial",
        "Hysterical",
        "Pickled",
        "Gaping",
        "Cyborg",
        "Toasted",
        "Hydrophobic",
        "Heartless",
        "Alcoholic",
        "Hungover",
        "Kentucky Fried",
        "Blue-Eyes White",
        "Red-Eyes Black",
        "Committed and Pashuned",
        "Rowan-faced",
        "Pun-tastic",
        "Homeless",
        "Cautiously Evasive",
        "Nike-Worshipping",
        "Mysterious",
        "Baby Brain"
    ]

    nouns = [
        "Cats",
        "Dogs",
        "Bears",
        "Motsons",
        "Pelicans",
        "CuntSmashers",
        "FIX Engines",
        "Tigers",
        "Bananas",
        "Capybaras",
        "Rowans",
        "FartBlasters",
        "PicklePickers",
        "PeckerHandlers",
        "Rats",
        "Hullaballoos",
        "Whippersnappers",
        "Poppycocks",
        "Otters",
        "FartSplitters",
        "PoopCollectors",
        "Donkeys",
        "Smurfs",
        "Mushrooms",
        "Bullets",
        "Clowns",
        "Aliens",
        "Plebs",
        "Pythons",
        "Bums",
        "Magicians",
        "Infants",
        "In-laws",
        "Convicts",
        "Antarcticans",
        "Mormons",
        "Antelopes",
        "Beekmeyers",
        "Plumbers",
        "Pirates",
        "Wizards",
        "Cheese Sandwiches",
        "Nobodies",
        "Alcoholics",
        "Chickens",
        "Dragons",
        "Bastards",
        "Nincompoops",
        "Harriotts",
        "Ronaldos",
        "Walids",
        "LEAN HOGS",
        "Pastor Freds",
        "Wangs",
        "Numberwangs"
    ]

    return "The " + random.choice(adjectives) + " " + random.choice(nouns)
