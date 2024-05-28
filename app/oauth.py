from authlib.integrations.flask_client import OAuth

oauth = OAuth()

def configure_oauth(app):
    oauth.init_app(app)
    oauth.register(
        name='riot',
        client_id=app.config['RSO_CLIENT_ID'],
        client_secret=app.config['RSO_CLIENT_SECRET'],
        access_token_url=app.config['RSO_BASE_URL'] + '/token',
        authorize_url=app.config['RSO_BASE_URL'] + '/authorize',
        client_kwargs={'scope': app.config['SCOPE']},
    )
