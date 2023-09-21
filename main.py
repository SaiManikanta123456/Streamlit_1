import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

st.header('Iris Flower Classifier')

st.markdown("""   
 It will classify among **Setosa** , **Versicolor** and **Verginica**
 """
)

st.sidebar.header("Input Features")

def f():
    sepal_length=st.sidebar.slider('Sepal Length',4.3,7.9,5.8)
    sepal_width=st.sidebar.slider('Sepal Width',2.0,4.4,3.4)
    petal_length = st.sidebar.slider('Petal Length',1.0,6.9,2.1)
    petal_width = st.sidebar.slider('Petal Width',0.1,2.5 , 0.5)
    d={
        'sepal_length' : sepal_length,
        'sepal_width':sepal_width,
        'petal_length':petal_length,
        'petal_width' : petal_width
    }
    features=pd.DataFrame(d,index=[0])

    return features

df=f()

st.write('User Inputted Values')

st.write(df)



data=load_iris()

x=data.data
y=data.target

m=RandomForestClassifier(n_estimators=5)

m.fit(x,y)

predictions=m.predict(df)

st.write(data.target_names[predictions])

