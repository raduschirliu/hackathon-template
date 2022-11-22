import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from src.models import db
from src import util

# Load environment variables
load_dotenv()

# Example backend call
util.example()

# Setup Flask and variables
port = int(os.getenv('PORT', 8000))
app = Flask(__name__)

# Setup CORS config
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

# Setup database config
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Silence the deprecation warning
db.init_app(app)
app.app_context().push()

## Create all tables defined in src/models.py
db.create_all()

# Routes
@app.route('/')
@cross_origin()
def hello_world():
    return 'hello, world'

# Main
if __name__ == '__main__':
    app.run(port=port, threaded=True)