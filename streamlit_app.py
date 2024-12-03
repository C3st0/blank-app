import streamlit as st
import numpy as np
import pandas as pd

df = pd.DataFrame(
    np.random.randn(10, 3),
    columns=['a', 'b', 'c']
)
df["pos"] = df["a"]>0 

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

edited_df = st.data_editor(df)
