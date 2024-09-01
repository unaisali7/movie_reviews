import streamlit as st
import joblib

model=joblib.load("review.pkl")

label = {'positive':'good', 'negative':'not that good'}

st.title("MOVIE REVIEW ANALYSIS")

user_input = st.text_area("Enter your review here:")

if st.button("analyse"):
    prediction=model.predict([user_input])[0]
    print(user_input)
    predicted_label=label[prediction]
    print("Predicted label:"+str(predicted_label))
    st.info(f"The movie is {str(predicted_label)}")
