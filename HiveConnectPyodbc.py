import pyodbc

import pandas as pd

with pyodbc.connect("DSN=Hive_Con", autocommit=True) as conn:
    df = pd.read_sql_query("select * from vega_data.tmp", conn)

# from sqlalchemy.engine import URL
# connection_string = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=dagger;DATABASE=test;UID=user;PWD=password"
# connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
#
# from sqlalchemy import create_engine
# engine = create_engine(connection_url)