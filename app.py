import streamlit as st
import pickle

# load model
with open("nlp_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("NLP Prediction App")

text = st.text_area("Enter Text")

if st.button("Predict"):
    if text.strip() != "":
        prediction = model.predict([text])
        st.success(f"Prediction: {prediction[0]}")
    else:
        st.warning("Please enter some text")
