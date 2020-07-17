'''
Small module for insult functionality.

Contains a function for generating a random insult, and a function
for turning that insult into a full sentence.
'''

import random

def insult_part():
    '''
    Concatenate an adjective with a noun and return the insult as a string.
    '''

    adjectives = ("aggressive", "aloof", "arrogant", "belligerent",
                "big-headed", "bitchy", "boastful", "bone-idle",
                "boring", "bossy", "callous", "cantankerous",
                "careless", "changeable", "clinging", "compulsive",
                "conservative", "cowardly", "cruel", "cunning",
                "cynical", "deceitful", "detached", "dishonest",
                "dogmatic", "domineering", "finicky", "flirtatious",
                "foolish", "foolhardy", "fussy", "greedy",
                "grumpy", "gullible", "harsh", "impatient",
                "impolite", "impulsive", "inconsiderate", "inconsistent",
                "indecisive", "indiscreet", "inflexible", "interfering",
                "intolerant", "irresponsible", "jealous", "lazy",
                "Machiavellian", "materialistic", "mean", "miserly",
                "moody", "narrow-minded", "nasty", "naughty",
                "nervous", "obsessive", "obstinate", "overcritical",
                "overemotional", "parsimonious", "patronizing", "perverse",
                "pessimistic", "pompous", "possessive", "pusillanimous",
                "quarrelsome", "quick-tempered", "resentful", "rude",
                "ruthless", "sarcastic", "secretive", "selfish",
                "self-centred", "self-indulgent", "silly", "sneaky",
                "stingy", "stubborn", "stupid", "superficial",
                "tactless", "timid", "touchy", "thoughtless",
                "truculent", "unkind", "unpredictable", "unreliable",
                "untidy", "untrustworthy", "vague", "vain",
                "vengeful", "vulgar", "weak-willed")

    nouns =  ("Amateur", "Animal", "Anorak", "Ape",
            "Ape covered in human flesh", "Apefucker", "Arse-licker", "Ass",
            "Ass-face", "Ass-hat", "Ass-kisser", "Ass-nugget",
            "Ass clown", "Assaholic", "Assbutt", "Assclown",
            "Assface", "Asshat", "Asshole", "Assmonkey",
            "Assmunch", "Asswagon", "Assweed", "Asswipe",
            "Aunt fucker", "Baby", "Backwoodsman", "Badass",
            "Badgerfucker", "Bag of dicks", "Bandit", "Barbarian",
            "Bastard", "Beast", "Beetlehead", "Beginner",
            "Bell-end", "Berk", "Bimbo", "Birdbrain",
            "Bitch", "Bitch Ass", "Bitch Ass Motherfucker", "Bitchboy",
            "Bitchface", "Bitchwad", "Bitchzilla", "Blockhead",
            "Blubber gut", "Bluntie", "Bogeyman", "Bonehead",
            "Boob", "Booby", "Boomer", "Bootlicker",
            "Boozer", "Bozo", "Bruh", "Buffoon",
            "Bugger", "Bum", "Bum chum", "Butthead",
            "Butthole", "Buttlicker", "Caveman", "Chauvinist",
            "Chav", "Cheater", "Chicken", "Chickenfucker",
            "Chode", "Chump", "Clown", "Cock",
            "Cockboy", "Cockburger", "Cockfucker", "Cockhead",
            "Cockholster", "Cockroach", "Con man", "Coomer",
            "Cougar", "Country bumpkin", "Cow", "Coward",
            "Crack whore", "Crackhead", "Craphole", "Creep",
            "Cretin", "Crook", "Cuckold", "Cumstain",
            "Cunt fart", "Cuntass", "Cuntbitch", "Cuntzilla",
            "Degenerate", "Desperado", "Dick", "Dick mouth",
            "Dick sniffer", "Dick weed", "Dickbag", "Dickbreath",
            "Dickface", "Dickfucker", "Dickhead", "Dildo",
            "Dimmadumbass", "Dimwit", "Ding-head", "Dingleberry",
            "Dinosaur", "Dipfuck", "Dirtbag", "Dirthead",
            "Dodo", "Dog", "Dolt", "Donkey",
            "Donkeyfucker", "Doofus", "Dope", "Douche bag",
            "Douche canoe", "Douche nozzle", "Douchelord", "Drunkard",
            "Duckfucker", "Dumbass", "Dumbbell", "Dumbo",
            "Dummy", "Dunce", "Duncebucket", "Earthworm",
            "Edgelord", "Egghead", "Egotist", "Eunuch",
            "Farmer", "Fart", "Fellow", "Fink",
            "Fish", "Fishwife", "Fixer", "Flake",
            "Fool", "Freak", "Fuck", "Fuck-wit",
            "Fuck noggin", "Fuck nugget", "Fuckass", "Fuckbait",
            "Fuckbucket", "Fucker", "Fuckhead", "Fucking bitch",
            "Fuckweasel", "Fuckwhistle", "Fuckwit", "Geebag",
            "Gimp", "Git", "Gobshite", "Gold digger",
            "Goof", "Goon", "Goose", "Gorilla",
            "Grouch", "Grumpy", "Helldog", "Hikikomori",
            "Hilding", "Hillbilly", "Hippie", "Ho",
            "Hobbledehoy", "Hoe", "Hooligan", "Hooplehead",
            "Horse's ass", "Horse's necktie", "Hosebag", "Hypocrite",
            "Idiot", "Ignoramus", "Imbecile", "Inbred",
            "Intercourser", "Jackass", "Jackwagon", "Jelly",
            "Jerk", "Jerkwad", "Joker", "Junkie",
            "Keyboard warrior", "Lamebrain", "Landwhale", "Lard Ass",
            "Lard face", "Liar", "Lobotomite", "Loser",
            "Low-life", "Lunatic", "Lunkhead", "Lurdane",
            "Lush", "Mackerel", "Madman", "Maggot",
            "Mamzer", "Meanie", "Megadouche", "Minx",
            "Mongoose", "Monkey", "Monster", "Moron",
            "Motherfucker", "Mouthbreather", "Mucky pup", "Muppet",
            "Mutant", "Mutt", "Ne'er-do-well", "Neanderthal",
            "Neckbeard", "Nerd", "Nerf herder", "Nimrod",
            "Nincompoop", "Ninny", "Nitwit", "Nobody",
            "Non", "Nonce", "Noob", "Noodle",
            "Numbnuts", "Numbskull", "Numpty", "Numskull",
            "Oaf", "Oddball", "Ogre", "Oompa loompa",
            "Orphan", "Outlaw", "Oxygen Thief", "Pack",
            "Pain in the ass", "Pariah", "Peasant", "Pee Mom",
            "Penchod", "Pencil dick", "Penis face", "Pervert",
            "Pig", "Pigfucker", "Piggy-wiggy", "Pillock",
            "Pinhead", "Pirate", "Pissface", "Pleb",
            "Porno freak", "Prick", "Pseudo-intellectual", "Pube flosser",
            "Puppet", "Quack", "Querulant", "Rat",
            "Ratcatcher", "Ratfink", "Redneck", "Reject",
            "Riff-raff", "Roaster", "Robot", "Rowdy",
            "Rudesby", "Ruffian", "Runt", "Sadist",
            "Saprophyte", "Sausage-masseuse", "Scumbag", "Scumhead",
            "Scumlord", "Scuzzbag", "Serf", "Sewer rat",
            "Shark", "Sheepfucker", "Sheepshagger", "Shill",
            "Shit-eater", "Shit-for-brains", "Shit stain", "Shitass",
            "Shitbucket", "Shitehawk", "Shitfuck", "Shithead",
            "Shitneck", "Shitnugget", "Shitsack", "Shitter",
            "Shitweasel", "Shyster", "Simp", "Simpleton",
            "Skank", "Skunk", "Skunkfucker", "Slave",
            "Sleeze", "Sleeze bag", "Slob", "Snail",
            "Snake", "Snob", "Snollygoster", "Snot",
            "Snotball", "Snowflake", "Son of a bitch", "Son of a motherless goat",
            "Sphincter", "Square", "Stinker", "Stinkhole",
            "Swindler", "Swine", "Sycophant", "Theatre kid",
            "Thief", "Thundercunt", "Titbag", "Toad",
            "Tool", "Tree hugger", "Troglodyte", "Troll",
            "Trollface", "Turd", "Turdball", "Twatwaffle",
            "Twerp", "Twit", "Ugly ass", "Unclefucker",
            "Vagina cleaner", "Vampire", "Vandal", "Varmint",
            "Vermin", "Wacko", "Wallflower", "Wank stain",
            "Wanker", "Weirdo", "Whore", "Windfucker",
            "Windsucker", "Worm", "Wretch", "Xenophobe",
            "Yahoo", "Yes-man", "Yonker", "Zitface",
            "Zounderkite")

    # Concatenate the random adjectives and nouns
    insult_template = (random.choice(adjectives).lower()
                      + ' '
                      + random.choice(nouns).lower()
                      + '.')

    # Return the string
    return insult_template


def insult(template):
    '''
    Take a string and append it to the start of an insult.
    This makes it easy to reuse the insults in other contexts
    while still easily returning an insult as a full sentence.
    '''

    # Possible beginnings to the insults
    start = ('Can it {}, you ',
             'Cool it {}, you ',
             'Shut up {}, you ',
             'Cut it out {}, you ',
             'I\'ve heard enough out of you {}, you ',
             'Silence yourself {}, you ',
             '{}... spare me, you ',
             '{}, you sound like a ',
             '{}, quit being a ')

    return random.choice(start) + template
