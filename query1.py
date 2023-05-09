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






