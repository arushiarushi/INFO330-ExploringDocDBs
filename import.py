import sqlite3
from pymongo import MongoClient

# Establishing the connection to SQLite
sql_conn = sqlite3.connect("pokemon.sqlite")
sql_cursor = sql_conn.cursor()

# Establishing the connection to MongoDB
mongoClient = MongoClient("mongodb://localhost/pokemon")
# Accessing the pokemon DB base
pokemonDB = mongoClient['pokemondb']

# Loop through each Pokemon in the SQLite database
for row in sql_cursor.execute("SELECT name FROM pokemon"):
    # Retrieve information for the current Pokemon
    query = '''
    SELECT p.id, p.name, p.pokedex_number, t.type1, t.type2, p.hp, p.attack, p.defense, p.speed, p.sp_attack, p.sp_defense, a.name as a_name
    FROM pokemon AS p
    JOIN pokemon_types_view t ON p.name = t.name
    JOIN pokemon_abilities pa ON p.id = pa.pokemon_id
    JOIN ability a ON pa.ability_id = a.id
    WHERE p.name = ?
    '''
    sql_cursor.execute(query, (row[0],))
    pokemon_rows = sql_cursor.fetchall()

    # Create a new collection for the current Pokemon
    pokemon_collection = pokemonDB[row[0].lower()]

    # Create a document for each row of data and insert it into the current Pokemon's collection
    for pokemon_row in pokemon_rows:
        pokemon_dict = {
            "name": pokemon_row[0],
            "pokedex_number": pokemon_row[1],
            "types": [pokemon_row[2], pokemon_row[3]],
            "hp": pokemon_row[4],
            "attack": pokemon_row[5],
            "defense": pokemon_row[6],
            "speed": pokemon_row[7],
            "sp_attack": pokemon_row[8],
            "sp_defense": pokemon_row[9],
            "abilities": [pokemon_row[10], pokemon_row[11]],
        }
        pokemon_collection.insert_one(pokemon_dict)

