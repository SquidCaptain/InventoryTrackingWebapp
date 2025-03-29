from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Fetch variables
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

## Flask (and extensions) config class
class Config:
    DEBUG = False

    # Construct the SQLAlchemy connection string
    #DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"
    SQLALCHEMY_DATABASE_URI = os.getenv("POSTGRES_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False