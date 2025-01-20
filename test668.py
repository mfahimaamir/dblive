import streamlit as st
import pyodbc
import pandas as pd
#conn_str=('DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=mfa.accdb;')

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=c:/iqra/mfa.accdb;'
)

#conn_str = pyodbc.connect("DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};" + \
 #                     "DBQ=TESTDB/mfa.accdb;")
st.header("Muhammad is the best in all over thuniverses")
connm = pyodbc.connect(conn_str)
cursorm = connm.cursor()
query = "SELECT * FROM Payments"
dataf = pd.read_sql(query, connm)
mm = st.dataframe()
st.write(dataf)

