import pandas as pd
from sqlalchemy import create_engine 

engine = create_engine('sqlite:///../db/galaxy-catalog.db', echo=False)

messier_df = pd.read_json("../raw_data/messier-catalog.json")

json_fields = messier_df.fields.to_json()
df = pd.read_json(json_fields).T

df = df.drop(columns=["image_url", "mag"])

df.to_sql(name="messier_catalog", con=engine)