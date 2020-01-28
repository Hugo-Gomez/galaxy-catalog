#IMPORTS

from flask import Flask, request
import json
from waitress import serve
from flask_cors import CORS, cross_origin
import traceback

from sqlalchemy import create_engine

from utils.requetes import *

#APP CONFIG

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

#connecteur sqlite
engine = create_engine('sqlite:///db/galaxy-catalog.db', echo=False)

#ROUTES

@app.route('/')
def hello_world():
   return 'Hello, World'

cors_gobi = CORS(app, resources={r"/get_object_by_id": {"origins": "*"}})

@app.route('/get_object_by_id', methods=["GET"])
@cross_origin(origin='*', headers=['Content-Type'])
def get_object_by_id():
    try:
        obj_id = request.args.get('id')
        data = get_obj_by_id(obj_id)
        resp  = json.dumps(data)
        return resp

    except Exception:
        return traceback.format_exc()

#APP

if __name__ == "__main__":
   app.run(debug=True) ##Replaced with below code to run it using waitress
   # serve(app, host='0.0.0.0', port=2727)
