from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import httpx
import random
import requests
import sort
import aiohttp

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # or 3000 if using Create React App
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Pokemon(BaseModel):
    pokemon: str
    dex_number: int
    sprite: str

class ID(BaseModel):
    id : int


BASE_URL = "https://pokeapi.co/api/v2"

@app.post("/show-step")
async def show_step():

    return 


@app.post("/collect-pokemon")
async def collect_pokemon():
    dex_lst = [random.randint(1, 100) for _ in range(10)]
    pokemon_list = []

    async with aiohttp.ClientSession() as session:
        for id in dex_lst:
            url = f"https://pokeapi.co/api/v2/pokemon/{id}/"
            async with session.get(url) as response:
                if response.status != 200:
                    print(f"Error: Could not find Pokémon '{id}'")
                    continue
                data = await response.json()
                pokemon_list.append(data["name"])

    print('pokedex list', dex_lst)
    print('----------------')
    print('pokemon list', pokemon_list)
    print('----------------')

    return {
        "unsorted_pokedex_numbers": dex_lst,
        "unsorted_pokemon_list": pokemon_list
    }

@app.get("/test")
def test():
    try:
        url = "https://pokeapi.co/api/v2/pokemon/1/"
        response = requests.get(url)

        if response.status_code != 200:
            return {"error": f"Pokémon not found (status: {response.status_code})"}

        data = response.json()
        return {"name": data["name"]}

    except Exception as e:
        return {"error": str(e)}
