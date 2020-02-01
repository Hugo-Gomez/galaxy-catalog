from app import engine
from flask import jsonify

# Generic method to collect object
def get_object(catalog_name, attr, attr_value):
    try:
        data = get_obj_by_attr(catalog_name, attr, attr_value)
        resp  = jsonify(data)
        return resp
    except Exception:
        return "<div>Invalid Request, find help at <a href='/'>this page</a>.</div>"

# Get object by attribute
def get_obj_by_attr(catalog_name, attr, attr_value):
    data = engine.execute(f'SELECT * FROM {catalog_name}_catalog WHERE {attr} = "{attr_value}";')
    d, a = {}, []
    for rowproxy in data:
        for column, value in rowproxy.items():
            d = {**d, **{column: value}}
        a.append(d)

    return a