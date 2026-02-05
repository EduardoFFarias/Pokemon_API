#%%
import pandas as pd
import requests

LIMIT = 50
url = f"https://pokeapi.co/api/v2/pokemon?limiti={LIMIT}"

response = requests.get(url)
data = response.json()

pokemon_lista = data["results"]

dados_pokemon = []
for pokemon in pokemon_lista:
    url_detalhe = pokemon["url"]

    url_detalhe = requests.get(url_detalhe).json()

    dados_pokemon.append({
        "nome": url_detalhe["name"],
        "id": url_detalhe["id"],
        "altura": url_detalhe["height"],
        "peso": url_detalhe["weight"],
        "experiencia_base": url_detalhe["base_experience"],
        "tipo1": url_detalhe["types"][0]["type"]["name"],
        "tipo2": url_detalhe["types"][1]["type"]["name"] if len(url_detalhe["types"]) > 1 else None
    })

#%%
df = pd.DataFrame(dados_pokemon)
df["id"] = df["id"].astype(int)
df["imagem"] = df["id"].apply(
    lambda x: f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{x}.png"
)

df.to_csv("pokemon_api.csv", index=False, encoding="utf-8")
#%%
df