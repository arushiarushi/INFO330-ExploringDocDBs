from pymongo import MongoClient

# Connect to MongoDB
mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']


#Query 3
print("query 3")
overgrow = {'abilities': 'Overgrow'}
pokemon_overgrow = pokemonColl.find(overgrow)
for pokemon in pokemon_overgrow:
    print(pokemon)

