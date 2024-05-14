import pandas as pd
import notion_df

from flask import Flask, render_template, redirect, url_for, request, session
from zenora import APIClient
from config import HOST, BOT_TOKEN, CLIENT_SECRET, OAUTH_URL, REDIRECT_URI, NOTION_TOKEN, NOTION_WEEKS_DATABASE_URL, NOTION_PLAYERS_DATABASE_URL, NOTION_DRAFTS_DATABASE_URL, SEASON, LEAGUE
from utils.time import get_split_and_week_and_time

notion_df.pandas()
app = Flask(__name__)
app.secret_key = "super secret key"
client = APIClient(BOT_TOKEN, client_secret=CLIENT_SECRET)

weeks         = pd.read_notion(NOTION_WEEKS_DATABASE_URL, api_key=NOTION_TOKEN)
weeks['From'] = pd.to_datetime(weeks['From'])

players = pd.read_notion(NOTION_PLAYERS_DATABASE_URL, api_key=NOTION_TOKEN)

TOPS = players[players.Role == 'top'].to_dict(orient='records')
JNGS = players[players.Role == 'jng'].to_dict(orient='records')
MIDS = players[players.Role == 'mid'].to_dict(orient='records')
BOTS = players[players.Role == 'bot'].to_dict(orient='records')
SUPS = players[players.Role == 'sup'].to_dict(orient='records')

SPLIT, WEEK, TIME = get_split_and_week_and_time(weeks)

@app.route('/')
def home():

    access_token = session.get("access_token")

    if not access_token:
        return render_template("home.html")

    bearer_client = APIClient(access_token, bearer=True)
    current_user = bearer_client.users.get_current_user()

    return render_template('dashboard.html', USER=current_user, SEASON=SEASON, LEAGUE=LEAGUE, SPLIT=SPLIT, WEEK=WEEK, TIME=TIME, TOPS=TOPS, JNGS=JNGS, MIDS=MIDS, BOTS=BOTS, SUPS=SUPS)
    
@app.route("/login")
def login():
    return redirect(OAUTH_URL)

@app.route("/logout")
def logout():
    """session.pop("access_token")
    return redirect("/")"""
    access_token = session.get("access_token")

    if not access_token:
        return render_template("home.html")

    bearer_client = APIClient(access_token, bearer=True)
    current_user = bearer_client.users.get_current_user()
    return render_template('leaderboard.html', USER=current_user, SEASON=SEASON, LEAGUE=LEAGUE, SPLIT=SPLIT, WEEK=WEEK)

@app.route("/oauth/callback")
def oauth_callback():
    code = request.args["code"]
    access_token = client.oauth.get_access_token(code, redirect_uri=REDIRECT_URI).access_token
    session["access_token"] = access_token
    return redirect("/")

@app.route("/roster", methods = ["post"])
def roster():
    data = request.get_json()
    print(data)

    draft = pd.DataFrame(
        columns = ['user_id', 'username', 'league', 'week', 'top', 'jng', 'mid', 'bot', 'sup', '-'],
        data    = [(data['user_id'], data['username'], LEAGUE, WEEK, data['roster']['top'], data['roster']['jng'], data['roster']['mid'], data['roster']['bot'], data['roster']['sup'], '')]     
    )
    draft.to_notion(NOTION_DRAFTS_DATABASE_URL, api_key=NOTION_TOKEN)
    return 'TODO'

if __name__ == '__main__':
    app.run(host=HOST, port=5000, debug=True)


