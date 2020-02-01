## IMPORTS ##

# App
from flask import Flask, request, render_template
import json
from waitress import serve
from flask_cors import CORS, cross_origin
import traceback
# Database
from sqlalchemy import create_engine
# Utilitaries
from utils.requests import *

# App configuration
app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

# sqlite connector
engine = create_engine('sqlite:///db/galaxy-catalog.db', echo=False)

## ROUTES ##

# Attributes that can be used as filter
# Format = filter_name : column_name
attr_for_filtering = {
    "constellation": "const",
    "discoverer": "decouvreur",
    "year": "annee",
    "distance": "distance",
    "english_name": "english_name_nom_en_anglais",
    "french_name": "french_name_nom_francais",
    "latin_name": "latin_name_nom_latin",
    "ra": "ra"
}

# guide page
@app.route('/')
def index():
    return render_template('index.html', filters=attr_for_filtering)

# TODO : investigate CORS
# cors_gobi = CORS(app, resources={r"/get_object_by_id": {"origins": "*"}})

# Get object by catalog and by Messier ID
@app.route('/<catalog_name>/object/<obj_id>/', methods=["GET"])
@cross_origin(origin='*', headers=['Content-Type'])
def get_object_by_id(catalog_name, obj_id):
    return get_object(catalog_name, "messier", obj_id)

# Get objects by filtering
@app.route('/<catalog_name>/objects', methods=["GET"])
@cross_origin(origin='*', headers=['Content-Type'])
def get_objects_by_filtering(catalog_name):
    args = request.args
    attr, attr_value = None, None
    if len(args) == 1 and next(iter(args)) in attr_for_filtering.keys():
        attr = attr_for_filtering[next(iter(args))]
        attr_value = args[next(iter(args))]
    return get_object(catalog_name, attr, attr_value)

## APP ##
if __name__ == "__main__":
    # Development
    app.run(debug=True)

    # Production
    # serve(app, host='0.0.0.0', port=2727)
