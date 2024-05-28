from authlib.integrations.flask_client import OAuth
import os

oauth = OAuth()

def configure_oauth(app):
    oauth.init_app(app)
    oauth.register(
        name='riot',
        client_id=os.getenv('RSO_CLIENT_ID'),
        client_secret=os.getenv('RSO_CLIENT_SECRET'),
        access_token_url=f"{os.getenv('RSO_BASE_URL')}/token",
        authorize_url=f"{os.getenv('RSO_BASE_URL')}/authorize",
        client_kwargs={'scope': os.getenv('SCOPE')},
    )
