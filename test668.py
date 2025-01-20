import streamlit as st
import pyodbc
import pandas as pd
conn_str=('DRIVER={Microsoft Access Driver (*.accdb)};DBQ=mfa.accdb;')
#conn_str = (
#    r'DRIVER={Microsoft Access Driver (*.accdb)};'
#    r'DBQ=mfa.accdb;'
)
connm = pyodbc.connect(conn_str)
cursorm = connm.cursor()
query = "SELECT * FROM Payments"
dataf = pd.read_sql(query, connm)
mm = st.dataframe()
st.write(dataf)
