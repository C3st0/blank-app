import streamlit as st
import numpy as np
import pandas as pd
from datetime import time, datetime

rows = []
row1 = {"matin_arrivée":datetime(2024,12,2, 8,20),
        "matin_départ":datetime(2024,12,2,12,15),
        "aprèm_arrivée":datetime(2024,12,2,13,00),
        "aprèm_départ":datetime(2024,12,2,17,15)
        }

rows.append(row1)
row2 = {"matin_arrivée":datetime(2024,12,2, 8,15),
        "matin_départ":datetime(2024,12,2,12,30),
        "aprèm_arrivée":datetime(2024,12,2,13,00),
        "aprèm_départ":datetime(2024,12,2,17,00)
        }

rows.append(row2)

df = pd.DataFrame().from_dict(rows)

df["Durée"] = ((df["matin_départ"] - df["matin_arrivée"])+ \
                ( df["aprèm_départ"] - df["aprèm_arrivée"])).dt.seconds

df["Durée"] = (df["Durée"]/3600).round(2)

df["Date"] = df["matin_départ"].dt.date
df["matin_départ"] = df["matin_départ"].dt.time
df["matin_arrivée"] = df["matin_arrivée"].dt.time
df["aprèm_départ"] = df["aprèm_départ"].dt.time
df["aprèm_arrivée"]= df["aprèm_arrivée"].dt.time

df.rename(columns = {'matin_arrivée':'mat_arr',
                     'matin_départ':'mat_dép',
                     'aprèm_arrivée':'apr_arr',
                     'aprèm_départ':'apr_dép'}, inplace=True)

st.title("Time management")
st.write(
    f"Daily time spent. Total worked {df['Durée'].sum()}"
)

edited_df = st.data_editor(df)
