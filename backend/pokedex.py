#for implementation based on how much i love each pokemon


# pokemon_gen_1 = {
#     "bulbasaur": 0,
#     "ivysaur": 0,
#     "Venusaur": 0,
#     "Charmander":0
# }
import requests
response = requests.get("https://pokeapi.co/api/v2/pokemon/1/")
print(response.status_code)
print(response.json())