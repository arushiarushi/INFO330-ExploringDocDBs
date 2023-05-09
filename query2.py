from pymongo import MongoClient

# Connect to MongoDB
mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']


#Query2
print("Query 2")
attack = {"attack": {"$gt": 150}}
pokemonAttack = pokemonColl.find(attack)
for pokemon in pokemonAttack:
    print(pokemon)