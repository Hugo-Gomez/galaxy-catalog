#IMPORTS

from flask import Flask, request, jsonify
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
        resp  = jsonify(data)
        return resp

    except Exception:
        return traceback.format_exc()

cors_gobc = CORS(app, resources={r"/get_object_by_const": {"origins": "*"}})

@app.route('/get_object_by_const', methods=["GET"])
@cross_origin(origin='*', headers=['Content-Type'])
def get_object_by_const():
    try:
        const = request.args.get('const')
        data = get_obj_by_const(const)
        resp  = jsonify(data)
        return resp

    except Exception:
        return traceback.format_exc()

cors_gobd = CORS(app, resources={r"/get_object_by_dec": {"origins": "*"}})

@app.route('/get_object_by_dec', methods=["GET"])
@cross_origin(origin='*', headers=['Content-Type'])
def get_object_by_dec():
    try:
        dec = request.args.get('dec')
        data = get_obj_by_dec(dec)
        resp  = jsonify(data)
        return resp

    except Exception:
        return traceback.format_exc()

#APP

if __name__ == "__main__":
   # app.run(debug=True) ##Replaced with below code to run it using waitress
   serve(app, host='0.0.0.0', port=2727)
