import pandas as pd
import json
import sqlite3
from sqlalchemy import create_engine

with open("database.json") as f:
    #openen van json en vertalen naar een df
    data = json.load(f)
    df = pd.DataFrame(data)

    #maken van sql connectie, db is leeg
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    df.to_sql("data",conn)

    engine = create_engine("sqlite://database2.db",echo=False)
    df.to_sql("data",engine)
