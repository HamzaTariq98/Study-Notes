import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

np.random.seed(5)
x = np.expand_dims(np.linspace(0,100,50),axis = -1)
y = np.ndarray.flatten(x) + 30*np.random.rand(50)

df = pd.DataFrame({
    'x': np.ndarray.flatten(x),
    'y':y
})
st.header('Data Exploration')

df

'Describe data'


st.write(df.describe())


st.header('Model Training')
model = LinearRegression()

if st.checkbox('Train Model'):
    model.fit(x,y)
    predictions = model.predict(x)
    df['y_pred'] = predictions
    st.line_chart(df.set_index('x'))

    st.header('Perform Predictions')

    st.subheader('Range Predictions')
    start = 0
    end = 200
    x1_range = st.slider('Prediction Range',start,end,(start,end))
    x1 = np.expand_dims(np.arange(x1_range[0],x1_range[1]),axis = -1)
    y_pred = model.predict(x1)

    if st.button('Predict'):
        fig ,ax = plt.subplots()
        ax.plot(x,y,label='Actual Data')
        ax.plot(x1,y_pred,label='Predictions') 
        ax.legend()
        st.pyplot(fig)

    st.subheader('Point Prediction')
    x_data = st.number_input('x')
    if x_data:
        st.write(f'yr prediction value is {model.predict([[x_data]])[0]:.2f}')




