from flask import Blueprint, redirect, url_for, session, render_template
from .oauth import oauth
from .utils import fetch_valorant_stats, fetch_player_info, fetch_leaderboard

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/login')
def login():
    redirect_uri = url_for('main.authorize', _external=True)
    return oauth.riot.authorize_redirect(redirect_uri)

@main.route('/authorize')
def authorize():
    token = oauth.riot.authorize_access_token()
    user_info = oauth.riot.parse_id_token(token)
    session['user'] = user_info
    return redirect(url_for('main.dashboard'))

@main.route('/dashboard')
def dashboard():
    user = session.get('user')
    if user:
        player_info = fetch_player_info(user['gameName'], user['tagLine'])
        leaderboard = fetch_leaderboard('current_act_id')  # Replace 'current_act_id' with the actual act ID
        stats = fetch_valorant_stats(user['sub'])
        return render_template('dashboard.html', user=user, player_info=player_info, leaderboard=leaderboard, stats=stats)
    return redirect(url_for('main.login'))
