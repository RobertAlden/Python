from random import randint

characters = {
"Mario":3,
"Bowser":3,
"Peach":5,
"Yoshi":3,
"Donkey Kong":5,
"Captain Falcon":3,
"Fox":1,
"Ness":1,
"Ice Climbers":1,
"Samus": 3,
"Zelda":5,
"Link":5,
"Pikachu":3,
"Jigglypuff":5,
"Dr. Mario":5,
"Luigi":3,
"Ganondorf":5,
"Falco":1,
"Young Link":5,
"Pichu":3,
"Mewtwo":5,
"Mr. Game & Watch":5,
"Marth":5,
"Roy":1}

current_pool = randint(1000,10000)
draws = 10
chars = []
while len(chars) < draws:
    for k,v in characters.items():
        current_pool -= v
        if current_pool < 0:
            chars.append((k,v))
            characters[k] /= 1.5
            for a in characters:
                if a != k or a not in chars:
                    characters[a] *= 1.2
                    characters[a] = round(characters[a],3)
            current_pool = randint(100,1000)
            break

numeral = ""
ordinal = ""
for i,c in enumerate(chars):
    if i == 0:
        ordinal = "st"
    elif i == 1:
        ordinal = "nd"
    elif i == 2:
        ordinal = "rd"
    else:
        ordinal = "th"
    numeral = str(i+1)
    print(f"{numeral}{ordinal}: {c[0]} at a draw score of {c[1]}!")

print("________________")
for k,v in characters.items():
    print(f"{k} --- {v}")

