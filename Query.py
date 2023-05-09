from pymongo import MongoClient

# Connect to MongoDB
mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']


#Query 1:
# Query 1
print("Query #1")
pikachu = pokemonColl.find({"name": "Pikachu"})
for pokemon in pikachu:
    print(pokemon)

#Query2
print("Query 2")
attack = {"attack": {"$gt": 150}}
pokemonAttack = pokemonColl.find(attack)
for pokemon in pokemonAttack:
    print(pokemon)

#Query 3
overgrow = {'abilities': 'Overgrow'}
pokemon_overgrow = pokemonColl.find(overgrow)
for pokemon in pokemon_overgrow:
    print(pokemon)




