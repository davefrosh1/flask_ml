import streamlit as st
import pandas as pd
import numpy as np
st.title('My first streamlit app')
df = pd.DataFrame(np.random.randint(1,100,20).reshape(4,5), columns=['a','b','c','d','e'])
st.write('here is my dataframe')
st.write(df)
st.line_chart(df['a'])
a = st.slider('what is your age',1,30,2)
st.write(f'you age is {a}')
