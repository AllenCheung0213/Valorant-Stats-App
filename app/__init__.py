from flask import Flask
from .config import Config
from .oauth import configure_oauth
from .routes import main as main_blueprint
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv()
    
    app = Flask(__name__, template_folder='../templates')
    print("Template folder:", app.template_folder)
    app.config.from_object(Config)
    
    configure_oauth(app)
    
    app.register_blueprint(main_blueprint)
    
    return app
