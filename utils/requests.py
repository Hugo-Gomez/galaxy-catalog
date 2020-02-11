from flask import jsonify, abort, Response
# Database
from sqlalchemy import create_engine

# sqlite connector
# dev
# engine = create_engine('sqlite:///db/galaxy-catalog.db', echo=False)
# prod
engine = create_engine('sqlite:////home/hugomez/galaxy-catalog/db/galaxy-catalog.db', echo=False)

# Generic method to collect object
def get_object(catalog_name, filter_dict):
    resp = []
    try:
        data = get_obj_by_filtering(catalog_name, filter_dict)
        resp  = jsonify(data)
    except Exception:
        return Response(
            "<div>Invalid Request, find help at <a href='/'>this page</a>.</div>", 
            status=400)
    if len(resp.json) == 0:
        return abort(404)
    else:
        return resp

# Get object by attribute
def get_obj_by_filtering(catalog_name, filter_dict):
    sql_req = f'SELECT * FROM {catalog_name}_catalog WHERE '
    for filter_key, filter_val in filter_dict.items():
        if filter_key == list(filter_dict.keys())[-1]:
            sql_req += f'{filter_key} = "{filter_val}";'
        else:
            sql_req += f'{filter_key} = "{filter_val}" AND '
    data = engine.execute(sql_req)
    d, a = {}, []
    for rowproxy in data:
        for column, value in rowproxy.items():
            d = {**d, **{column: value}}
        a.append(d)

    return a