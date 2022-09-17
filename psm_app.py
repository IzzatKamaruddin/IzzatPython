# -*- coding: utf-8 -*-
"""psm_app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tPPElwWBLkH2D3z58tkegF1q2eS-Fte8
"""

import streamlit as st
import pandas as pd
import sklearn 
from sklearn.naive_bayes import GaussianNB

df = pd.read_csv(r"Covid19_Prediction - ClassifactionBasedSpecies.csv")

st.write("""
# Simple Corona Species Prediction App
This app predicts the **Virus Sprecies** type!
""")

st.sidebar.header('User Input Parameters')
def user_input_features():
  Nucleus = st.sidebar.slider('Nucleus',0.0,1.0,0.5)
  Exosome = st.sidebar.slider('Exosome',0.0,1.0,0.5)
  Ribosome = st.sidebar.slider('Ribosome',0.0,1.0,0.5)
  Membrane = st.sidebar.slider('Membrane',0.0,1.0,0.5)
  Endoplasmic_Reticulum = st.sidebar.slider('Endoplasmic Reticulum',0.0,1.0,0.5)
  Cytosol = st.sidebar.slider('Cytosol',0.0,1.0,0.5)
  data = {'Nucleus': Nucleus,
            'Exosome': Exosome,
            'Ribosome': Ribosome,
            'Membrane': Membrane,
            'Endoplasmic_Reticulum': Endoplasmic_Reticulum,
            'Cytosol': Cytosol}

  features = pd.DataFrame(data,index = [0])
  return features

df = user_input_features

st.subheader("User Input Parameter")
st.write(df)

dataset = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/Covid19_Prediction - ClassifactionBasedSpecies.csv")
target = dataset["Species"]
input = dataset.drop("Species", axis = 1)

clf = GaussianNB()
clf.fit(input,target)

prediction = clf.predict(input)
prediction_proba = clf.predict_proba(input)

st.subheader('Species labels and their corresponding index number')
st.write(target)

st.subheader('Prediction')
st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)



