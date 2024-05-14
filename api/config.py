import os

HOST='0.0.0.0'
PORT = 5000
BOT_TOKEN = os.environ["BOT_TOKEN"]
CLIENT_SECRET = os.environ["CLIENT_SECRET"]
CLIENT_ID = os.environ["CLIENT_ID"]
REDIRECT_URI = f"http://localhost:{PORT}/oauth/callback"  # Your Oauth redirect URI
OAUTH_URL = f"https://discord.com/api/oauth2/authorize?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=code&scope=identify"
NOTION_TOKEN= os.environ["NOTION_TOKEN"]
NOTION_WEEKS_DATABASE_URL='https://www.notion.so/zapatone/f549c03002ef4235a45112a9e4a181da?v=97423d2261c040ae9a2b119e377cee01'
NOTION_PLAYERS_DATABASE_URL = 'https://www.notion.so/zapatone/d773150c37ea4ec1a2173febbf79adbb?v=d497378005c7442b8c52e84ed8fb87cb'
NOTION_DRAFTS_DATABASE_URL = 'https://www.notion.so/zapatone/47fe3d743d07424680ba9475603dd88e?v=08f38efad2af42489249a0901f2f9aa1'
SEASON = '01'
LEAGUE = 'LIT'