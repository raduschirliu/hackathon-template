import os
from dotenv import load_dotenv
from flask import Flask

load_dotenv()

port = int(os.getenv('PORT', 8000))
app = Flask('app')

@app.route('/')
def hello_world():
    return 'hello, world'

if __name__ == '__main__':
    app.run(port=port, threaded=True)