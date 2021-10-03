import logging
import requests
import json
from pokeCather import catPokemon
from messageBuilder import buildMessage

#Insert the bot token
TELEGRAM_TOKEN = ""


from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

requester = requests.get

#Separa o nome do pokemon
def normalizePoke(command):

    searchPoke = command.upper()
    searchPoke = searchPoke.replace("/POKEDEX ", "")
    searchPoke = searchPoke.lower()

    return searchPoke

def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Olá {user.mention_markdown_v2()}\!, Bem\-vindo\(a\) a TeleDex'
    )

    update.message.reply_text("Código fonte: https://github.com/LukaOliveira/PokedexOnTelegram")
    update.message.reply_text("\nPara buscar um pokemon,\ndigite /pokedex nomePokemon\n\nExemplo: /pokedex charizard")




def poke_command(update: Update, context: CallbackContext) -> None:

    #Verifica se um pokemon foi enviado junto ao comando
    if(" " in update.message.text):

        update.message.reply_text("Buscando Pokemon...")

        searchPoke = normalizePoke(update.message.text)

        pokeReturned = catPokemon(searchPoke)

        #Verifica se o pokemon foi encontrado
        if(pokeReturned != 0):
            update.message.reply_text(pokeReturned[0]["sprite"])
            update.message.reply_text(buildMessage(pokeReturned))
        else:
            update.message.reply_text("Pokemon não Encontrado...")
    else:
        update.message.reply_text("Para buscar um pokemon digite: \n\n/pokedex nomePokemon")
       


def main() -> None:
    updater = Updater(TELEGRAM_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("pokedex", poke_command))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()