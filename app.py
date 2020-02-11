## IMPORTS ##

# App
from flask import Flask, request, render_template
import json
from flask_cors import CORS, cross_origin
import traceback
# Utilitaries
from utils.requests import *

# App configuration
app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

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

# Get object by catalog and by Messier ID
@app.route('/<catalog_name>/object/<obj_id>/', methods=["GET"])
@cross_origin(origin='*', headers=['Content-Type'])
def get_object_by_id(catalog_name, obj_id):
    return get_object(catalog_name, "messier", obj_id.capitalize())

# Get objects by filtering
@app.route('/<catalog_name>/objects', methods=["GET"])
@cross_origin(origin='*', headers=['Content-Type'])
def get_objects_by_filtering(catalog_name):
    args = request.args
    filter_dict = {}
    for arg in args.items():
        filter_dict[attr_for_filtering[arg[0]]] = arg[1].capitalize()
    return get_object(catalog_name, filter_dict)

## APP ##
if __name__ == "__main__":
    # Development
    app.run(debug=True)
