from app import engine

def get_obj_by_id(obj_id) :
    data = engine.execute(f'SELECT * FROM messier_catalog WHERE messier = "{obj_id}";')

    d, a = {}, []
    for rowproxy in data:
        # rowproxy.items() returns an array like [(key0, value0), (key1, value1)]
        for column, value in rowproxy.items():
            # build up the dictionary
            d = {**d, **{column: value}}
        a.append(d)

    return a
