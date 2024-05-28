import requests
from flask import current_app

def fetch_valorant_stats(user_id):
    headers = {
        'Authorization': f'Bearer {current_app.config["DEPLOYMENT_API_KEY"]}',
    }
    response = requests.get(f'https://api.riotgames.com/val/stats/v1/{user_id}', headers=headers)
    if response.status_code == 200:
        stats = response.json()
        stats['tips'] = generate_tips(stats)
        return stats
    else:
        return None

def generate_tips(stats):
    tips = []
    if stats['headshot_percentage'] < 20:
        tips.append("Improve your headshot accuracy by practicing aim drills.")
    if stats['kd_ratio'] < 1:
        tips.append("Focus on improving your K/D ratio by playing more cautiously.")
    if stats['win_rate'] < 50:
        tips.append("Focus on your map awareness and teamwork to improve your win rate.")
    return tips

def fetch_player_info(game_name, tag_line):
    headers = {
        'X-Riot-Token': current_app.config["DEPLOYMENT_API_KEY"],
    }
    response = requests.get(
        f'https://api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}',
        headers=headers
    )
    if response.status_code == 200:
        return response.json()
    else:
        return None

def fetch_leaderboard(act_id):
    headers = {
        'X-Riot-Token': current_app.config["DEPLOYMENT_API_KEY"],
    }
    response = requests.get(
        f'https://api.riotgames.com/val/ranked/v1/leaderboards/by-act/{act_id}',
        headers=headers
    )
    if response.status_code == 200:
        return response.json()
    else:
        return None
