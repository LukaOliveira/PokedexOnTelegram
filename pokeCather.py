import requests
import json

requester = requests.get

def catPokemon(name):

    returned = requester("https://pokeapi.glitch.me/v1/pokemon/"+name)
        
    error = ""

    try:
        error = json.loads(returned.text)['error']
    except:
        error = ""
            
    if(error == ""):
        return json.loads(returned.text)
                    
    else:
        return 0