
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

np.random.seed(5)
x = np.expand_dims(np.linspace(0,100,50),axis = -1)
y = np.ndarray.flatten(x) + 30*np.random.rand(50)

df = pd.DataFrame({
    'x': np.ndarray.flatten(x),
    'y':y
})
st.write(df)
plt.plot(x,y)
plt.show()
st.line_chart(df['y'])

# x Slider
x = st.slider('x',0.0, 100.0, (25.0, 75.0))
st.write(f'x value is :{x}')

# text input
st.text_input("Your name", key="name")
st.write(st.session_state.name)

# Check Box state
show_data = st.checkbox('Show text again')
if show_data:
    st.write(f'Hello {st.session_state.name}')

gender = st.selectbox('gender',['Male','Female'])


add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)


