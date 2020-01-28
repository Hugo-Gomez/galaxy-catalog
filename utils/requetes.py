from app import engine

def get_obj_by_id(obj_id) :
    data = engine.execute(f'SELECT * FROM messier_catalog WHERE messier = "{obj_id}";')
    d, a = {}, []
    for rowproxy in data:
        for column, value in rowproxy.items():
            d = {**d, **{column: value}}
        a.append(d)

    return a

def get_obj_by_const(const) :
    data = engine.execute(f'SELECT * FROM messier_catalog WHERE const = "{const}";')
    d, a = {}, []
    for rowproxy in data:
        for column, value in rowproxy.items():
            d = {**d, **{column: value}}
        a.append(d)

    return a

def get_obj_by_sadecdecdec(dec) :
    data = engine.execute(f'SELECT * FROM messier_catalog WHERE decouvreur = "{dec}";')
    d, a = {}, []
    for rowproxy in data:
        for column, value in rowproxy.items():
            d = {**d, **{column: value}}
        a.append(d)

    return a
