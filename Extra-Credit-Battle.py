# To improve this script, I added a counter for the score of the first pokemon and second pokemon
# called p1_score and p2_score respectively. Based on this counter, I determined which pokemon
# won using if else statements. If the scores of p1 and p2 are the same(based on their
# stats), then the battle results in a tie.


import random
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

def fetch(pokemonid):
    return pokemonColl.find_one({"pokedex_number":pokemonid})

def battle(pokemon1, pokemon2):
    print("Let the Pokemon battle begin! ================")
    print("It's " + pokemon1['name'] + " vs " + pokemon2['name'])

    p1_score = 0
    p2_score = 0

    for stat in ['hp', 'attack', 'defense', 'speed', 'sp_attack', 'sp_defense']:
        if pokemon1[stat] > pokemon2[stat]:
            print(pokemon1['name'] + " has the advantage in " + stat)
            p1_score += 1

        elif pokemon2[stat] > pokemon1[stat]:
            print(pokemon2['name'] + "'s " + stat + " is superior")
            p2_score += 1
        else:
            print("Both Pokemon are evenly matched in " + stat)

    if p1_score > p2_score:
        print("Battle results: " + pokemon1['name'] + " wins!")
    elif p2_score > p1_score:
        print("Battle results: " + pokemon2['name'] + " wins!")
    else:
        print("The battle ended in a tie!")

def main():
    # Fetch two pokemon from the MongoDB database
    pokemon1 = fetch(random.randrange(801))
    pokemon2 = fetch(random.randrange(801))

    # Pit them against one another
    battle(pokemon1, pokemon2)

main()
