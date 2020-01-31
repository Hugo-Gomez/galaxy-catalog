import pandas as pd
from sqlalchemy import create_engine 

def push_json_to_db(catalog_name, catalog_file, columns_to_drop, engine):
    df = pd.read_json(f"../raw_data/{catalog_file}")

    json_fields = df.fields.to_json()
    df = pd.read_json(json_fields).T
    if len(columns_to_drop) > 0:
        df = df.drop(columns=columns_to_drop)

    df.to_sql(name=catalog_name, con=engine)

# SQLite engine
engine = create_engine('sqlite:///../db/galaxy-catalog.db', echo=False)

# Messier
messier_catalog_file = "messier-catalog.json"
messier_columns_to_drop = ["image_url", "mag"]

# General
gen_catalog_file = "general-catalog.json"
gen_columns_to_drop = ["image"]

# Messier
# push_json_to_db("messier_catalog", messier_catalog_file, messier_columns_to_drop, engine)
# General
push_json_to_db("general_catalog", gen_catalog_file, gen_columns_to_drop, engine)