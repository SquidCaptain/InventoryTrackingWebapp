from dotenv import load_dotenv
import os

## Flask (and extensions) config class
class Config:
    DEBUG = False

    # Load environment variables from .env
    load_dotenv()

    # Fetch variables
    USER = os.getenv("user")
    PASSWORD = os.getenv("password")
    HOST = os.getenv("host")
    PORT = os.getenv("port")
    DBNAME = os.getenv("dbname")

    # Construct the SQLAlchemy connection string
    DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:Pe0pVSqoPLk9NBQn@db.rppbyjhlvkfeltciqlen.supabase.co:5432/postgres?sslmode=require"
    SQLALCHEMY_TRACK_MODIFICATIONS = False