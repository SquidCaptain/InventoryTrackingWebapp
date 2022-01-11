import os
from pathlib import Path

from app import app
from app import db
from models import *

if not Path('./database.db').isfile():
    db.create_all()

if __name__ == '__main__':
    app.run()