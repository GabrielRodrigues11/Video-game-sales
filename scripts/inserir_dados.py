from dotenv import load_dotenv
import pandas as pd
import os
from sqlalchemy import create_engine

load_dotenv()  
senha = os.getenv("MYSQL_PASSWORD")

engine = create_engine(f"mysql+pymysql://root:{senha}@localhost/projetos")

videogame_df = pd.read_csv("dados/vgsales.csv")
videogame_df.to_sql("videogame_sales", engine, if_exists="append", index=False)
