from app import engine

def get_obj_by_attr(catalog_name, attr, attr_value):
    data = engine.execute(f'SELECT * FROM {catalog_name}_catalog WHERE {attr} = "{attr_value}";')
    d, a = {}, []
    for rowproxy in data:
        for column, value in rowproxy.items():
            d = {**d, **{column: value}}
        a.append(d)

    return a