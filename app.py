from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

from config import Config
#from orderedList import *

## --Flask App--
app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_POOL_SIZE'] = 10
app.config['SQLALCHEMY_MAX_OVERFLOW'] = 20

## --Database--
db = SQLAlchemy(app)
print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHEEEEEEEEEEELLLLLLLLLLLPPPPPPPPPPPPPPPPPP")
with app.app_context():
    db.create_all()