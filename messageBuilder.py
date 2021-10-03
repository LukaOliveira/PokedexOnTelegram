import json

def buildMessage(pokemon):
    finalMessage = ""

    finalMessage += "Nome: "+str(pokemon[0]['name'])+"\n\n"
    finalMessage += "Número na Pokedex: "+str(pokemon[0]['number'])+"\n\n"
    finalMessage += "Geração: "+str(pokemon[0]['gen'])+"ª\n\n"
    
    finalMessage += "Tipo(s): \n"

    for pokeType in pokemon[0]["types"]:
        finalMessage += "       "+pokeType+"\n"

    finalMessage += "\n"

    finalMessage += "Linha Evolutiva: \n"

    for state in pokemon[0]["family"]["evolutionLine"]:
        finalMessage += "       "+state+"\n"


    return finalMessage