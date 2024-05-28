import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    SESSION_COOKIE_NAME = 'valorant_login_session'
    RSO_BASE_URL = os.getenv('RSO_BASE_URL', 'https://auth.riotgames.com')
    RSO_CLIENT_ID = os.getenv('RSO_CLIENT_ID')
    RSO_CLIENT_SECRET = os.getenv('RSO_CLIENT_SECRET')
    APP_BASE_URL = os.getenv('APP_BASE_URL', 'http://localhost.riotgames.com:3000')
    APP_CALLBACK_PATH = os.getenv('APP_CALLBACK_PATH', '/oauth-callback')
    RESPONSE_TYPE = os.getenv('RESPONSE_TYPE', 'code')
    SCOPE = os.getenv('SCOPE', 'openid')
