import tkinter as tk
from tkinter import messagebox
import webbrowser
import fonctions_steam

# Fonction pour afficher une aide sur la récupération de la clé API Steam ou de l'ID Steam
def afficher_aide(url):
    webbrowser.open(url)

# Fonction pour calculer le temps de jeu et afficher le résultat dans une interface graphique
def calculer_temps_jeu():
    api_key = api_key_entry.get()
    steam_id = steam_id_entry.get()

    if not api_key or not steam_id:
        messagebox.showerror("Erreur", "Veuillez entrer votre clé API Steam et votre ID Steam.")
        return

    temps_total_jeu_minutes = fonctions_steam.get_playtime(api_key, steam_id)

    if temps_total_jeu_minutes is not None:
        heures, minutes = fonctions_steam.convert_playtime(temps_total_jeu_minutes)
        resultat_label.config(text=f"Temps total de jeu sur Steam : {heures} heures et {minutes} minutes.")

        annees, mois = convertir_temps_en_annees_et_mois(temps_total_jeu_minutes)
        resultat_annees_mois_label.config(text=f"Temps total de jeu sur Steam : {annees} années et {mois} mois.")
    else:
        messagebox.showerror("Erreur", "Impossible de récupérer le temps de jeu. Assurez-vous que votre ID Steam et votre clé API sont corrects.")

# Fonction pour convertir le temps total de jeu en années et mois
def convertir_temps_en_annees_et_mois(temps_total_minutes):
    temps_total_mois = temps_total_minutes / (30 * 24 * 60)  # Approximation de 30 jours par mois
    annees = int(temps_total_mois / 12)
    mois = int(temps_total_mois % 12)
    return annees, mois

# Créer la fenêtre principale
root = tk.Tk()
root.title("Calculateur de temps de jeu Steam")
root.geometry("540x220")

# Configuration du fond
root.configure(bg="#767f9c")

# Ajouter les widgets
api_key_frame = tk.Frame(root, bg="#767f9c")
api_key_frame.pack()

api_key_label = tk.Label(api_key_frame, text="Clé API Steam :", bg="#767f9c")
api_key_label.pack(side=tk.LEFT, padx=5, pady=5)

api_key_entry = tk.Entry(api_key_frame)
api_key_entry.pack(side=tk.LEFT, padx=5, pady=5)

steam_id_frame = tk.Frame(root, bg="#767f9c")
steam_id_frame.pack()

steam_id_label = tk.Label(steam_id_frame, text="ID Steam :", bg="#767f9c")
steam_id_label.pack(side=tk.LEFT, padx=5, pady=5)

steam_id_entry = tk.Entry(steam_id_frame)
steam_id_entry.pack(side=tk.LEFT, padx=5, pady=5)

calculer_button = tk.Button(root, text="Calculer son temps de jeu", command=calculer_temps_jeu)
calculer_button.pack(padx=5, pady=5)

resultat_label = tk.Label(root, text="", bg="#767f9c")
resultat_label.pack(padx=5, pady=5)

resultat_annees_mois_label = tk.Label(root, text="", bg="#767f9c")
resultat_annees_mois_label.pack(padx=5, pady=5)

# Lien hypertexte pour l'aide sur la récupération de la clé API Steam
lien_aide_cle_api = tk.Label(root, text="Récupérer la clé API Steam", fg="blue", cursor="hand2", bg="#767f9c")
lien_aide_cle_api.pack(padx=5, pady=5)
lien_aide_cle_api.bind("<Button-1>", lambda event: afficher_aide("https://steamcommunity.com/dev/apikey"))

# Lien hypertexte pour l'aide sur la récupération de l'ID Steam
lien_aide_id_steam = tk.Label(root, text="Récupérer l'ID Steam", fg="blue", cursor="hand2", bg="#767f9c")
lien_aide_id_steam.pack(padx=5, pady=5)
lien_aide_id_steam.bind("<Button-1>", lambda event: afficher_aide("https://help.steampowered.com/fr/faqs/view/2816-BE67-5B69-0FEC"))

# Lancer la boucle principale
root.mainloop()
