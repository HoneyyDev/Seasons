from secret import token # Importation de la variable TOKEN depuis secret.py.
from secret import logs_file # Importation de la variable logs_file depuis secret.py.
from secret import errors_messages_file # Importation de la variable errors_messages_file depuis secret.py.
from secret import prefix

import discord # Importation du module Discord permettant le fonctionnement du bot.
from discord.ext import commands
import logging # Importation du module logging permettant un retour des logs.

import os # Importation du module permettant de gérer les fichiers.
import shutil # Importation du module permettant de gérer les fichiers.



# Vérifie si un fichier log.txt existe. Si c'est le cas il est déplacé dans le dossier Logs sous le nom de LogX.
# Ici X est remplacé par un nombre. Plus celui-ci est élevé plus les logs sont récentes.
# Les dernières logs sont en dehors du dossier logs.
if os.path.exists(logs_file):
    log_number = 1
    while os.path.exists("Logs/logs" + str(log_number) + ".txt"):
        log_number += 1
    source = logs_file
    target = "Logs/logs" + str(log_number) +".txt"
    shutil.copy(source, target)
    os.remove(source)
    print("Le fichier de logs précédent vient d'être rangé dans le dossier \"Logs\".")
else:
    print("Il n'y avait aucun fichier de logs il a donc été créé.")


# Créé un fichier logs.txt à chaque fois que le bot s'éteint.
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename=logs_file, encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Importation des messages d'erreurs.
if os.path.exists(errors_messages_file):
    print(f"Le fichier {errors_messages_file} a bien été trouvé.")
else:
    print(f"Le fichier {errors_messages_file} est manquant.\nVous n'aurez donc pas de messages d'erreurs relatifs à votre code.\n")


client = discord.Client()

@client.event
async def on_ready(): # Quand le bot est démarré.
    print('Vous êtes désormais connecté sur {0.user}'.format(client))
    await client.change_presence(status= discord.Status.do_not_disturb, activity= discord.Activity(type= discord.ActivityType.playing, name = "faire l'hélicobite"))
    

@client.event
async def on_message(message):
    if message.author == client.user:
        return


    if message.content.startswith(f'{prefix}me'):
        await message.channel.send(f"{message.author}")

    if message.content.startswith(f'{prefix}invite'):
        await message.channel.send("https://discord.gg/bdRHCjsvYV")

    if message.content.startswith(".puceau"):
        await message.channel.send("Puceau moi ? Sérieusement ^^ haha on me l avait pas sortie celle la depuis loooongtemps demande a mes potes si je suis puceau tu vas voir les réponses que tu vas te prendre XD rien que la semaine passee j ai niquer dont chuuuuut ferme la puceau de merde car toi tu m as tout tout l air d un bon puceau de merde car souvent vous etes frustrer de ne pas baiseR ses agreable de se faire un missionnaire ou un amazone avec une meuf hein ? tu peux pas répondre car tu ne sais pas ce que c ou alors tu le sais mais tu as du taper dans ta barre de recherche « missionnaire sexe » ou « amazone sexe » pour comprendre ce que c etait mdddrrr !! cest grave quoiquil en soit....pour revenir a moi, je pense que je suis le mec le moins puceau de ma bande de 11 meilleurs amis pas psk j ai eu le plus de rapport intime mais psk j ai eu les plus jolie femme que mes amis ses pas moi qui le dit, ses eux qui commente sous mes photos insta « trop belle la fille que tu as coucher avec hier en boite notamment! » donc après si tu veux :)")


client.run(token) # Se connecte avec le token secret. Localisé dans secret.py
