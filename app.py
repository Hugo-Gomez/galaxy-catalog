#IMPORTS

from flask import Flask, request
import json
from waitress import serve
from flask_cors import CORS, cross_origin
import traceback

from utils.JESUISCOLERE import multiple_dab

#APP CONFIG

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

#ROUTES

@app.route('/')
def hello_world():
   return 'Hello, World'


cors_dab = CORS(app, resources={r"/dab": {"origins": "*"}})

@app.route('/dab', methods=["GET"])
@cross_origin(origin='*',headers=['Content- Type'])
def dab():
    try:
        nb_dab = request.args.get('nb_dab')
        data = multiple_dab(nb_dab)
        resp  = json.dumps(data)
        return resp

    except Exception:
        return traceback.format_exc()

#APP

if __name__ == "__main__":
   app.run(debug=True) ##Replaced with below code to run it using waitress
   # serve(app, host='0.0.0.0', port=2727)
