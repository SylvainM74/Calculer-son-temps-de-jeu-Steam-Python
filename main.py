import fonctions_steam
import interface

# Demander à l'utilisateur de saisir sa clé API et son ID Steam
api_key = input("Veuillez entrer votre clé API Steam : ")
steam_id = input("Veuillez entrer votre ID Steam : ")

# Appel de la fonction pour récupérer le temps de jeu
temps_total_jeu = fonctions_steam.get_playtime(api_key, steam_id)

if temps_total_jeu is not None:
    heures, minutes = fonctions_steam.convert_playtime(temps_total_jeu)
    print(f"Temps total de jeu sur Steam : {heures} heures et {minutes} minutes.")
else:
    print("Impossible de récupérer le temps de jeu. Assurez-vous que votre ID Steam et votre clé API sont corrects.")
