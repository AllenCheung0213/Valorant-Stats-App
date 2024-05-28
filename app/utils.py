import requests
from flask import current_app

def fetch_valorant_stats(user_id):
    # Example function to fetch Valorant stats using Riot API
    headers = {
        'Authorization': f'Bearer {current_app.config["RSO_CLIENT_SECRET"]}',
        'X-Riot-Token': current_app.config['DEPLOYMENT_API_KEY']
    }
    response = requests.get(f'https://api.riotgames.com/val/stats/v1/{user_id}', headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None
