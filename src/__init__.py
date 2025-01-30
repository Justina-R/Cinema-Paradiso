from flask import Flask
from dotenv import load_dotenv
import os

# Loading API key and secret key for Flask app from .env file
load_dotenv()
api_key = os.getenv("TMDB_API_KEY")
secret_key = os.getenv("SECRET_KEY")
# Loading mail and password from .env file
mail_username = os.getenv("MAIL_USERNAME")
mail_password = os.getenv("MAIL_PASSWORD")

# Creates and configures an instance of the Flask app
def create_app() -> Flask:
    app = Flask(__name__, template_folder="../templates")
    app.config["SECRET_KEY"] = secret_key
    return app

