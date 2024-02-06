import requests

# Fonction pour récupérer le temps de jeu pour un utilisateur Steam
def get_playtime(api_key, steam_id):
    url = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={api_key}&steamid={steam_id}&format=json"
    
    response = requests.get(url)
    
    try:
        data = response.json()
    except:
        return None

    if "response" in data and "games" in data["response"]:
        playtime_total = sum(game["playtime_forever"] for game in data["response"]["games"])
        return playtime_total
    else:
        return None

# Fonction pour convertir le temps de jeu en heures et minutes
def convert_playtime(playtime_minutes):
    hours = playtime_minutes // 60
    minutes = playtime_minutes % 60
    return hours, minutes
