#%%
import requests
import pandas as pd
import json

# Quantos pokémons quer buscar
limite = 151  # pode aumentar depois

# Lista principal
lista_pokemon = []

# Buscar lista de pokémons
url_lista = f"https://pokeapi.co/api/v2/pokemon?limit={limite}"
resposta_lista = requests.get(url_lista).json()

for pokemon in resposta_lista["results"]:
    dados = requests.get(pokemon["url"]).json()
    
    stats = {stat["stat"]["name"]: stat["base_stat"] for stat in dados["stats"]}
    
    lista_pokemon.append({
        "id": dados["id"],
        "nome": dados["name"],
        "altura": dados["height"],
        "peso": dados["weight"],
        "experiencia_base": dados["base_experience"],
        "tipo1": dados["types"][0]["type"]["name"],
        "tipo2": dados["types"][1]["type"]["name"] if len(dados["types"]) > 1 else None,
        "imagem": dados["sprites"]["front_default"],
        
        # Stats
        "hp": stats.get("hp"),
        "attack": stats.get("attack"),
        "defense": stats.get("defense"),
        "special_attack": stats.get("special-attack"),
        "special_defense": stats.get("special-defense"),
        "speed": stats.get("speed")
    })
# Criar DataFrame
df = pd.DataFrame(lista_pokemon)
#%%
df.to_csv(r"P:\Projetos\Pokemon_API\pokemon_api.csv", index=False, encoding="utf-8")
print("Arquivo salvo com sucesso!")
