import streamlit as st
import pandas as pd
import numpy as np

st.title("My first cloud app")

st.write(" A simple Dataframe ")
df=pd.DataFrame(np.random.randn(10,2),columns=['Col1','Col2'])
st.dataframe(df)
