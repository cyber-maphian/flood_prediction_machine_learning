import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_icon="💧",
    page_title="Flood",
    initial_sidebar_state="expanded"
)

st.header("Flood Prediction Using Machine Learning.")
st.markdown("HAPPINESS OLATUNDE")
#tab
home,dataset,about = st.tabs(['Home','Dataset','About'])

with home:
    with st.form(key="flood"):
        #Rainfall	Max Temperature	Min Temperature	Relative Humidity	Flood
        rainfall = st.text_input("RainFall ")
        max_tem = st.text_input("Max Temperature ")
        min_tem = st.text_input("Min Temperature")
        rel_hum = st.text_input("Relative Humidity")
        submit = st.form_submit_button("Predict💧",type="primary")

        if submit:
                #list
            features = [float(rainfall),float(max_tem),float(min_tem),float(rel_hum)]
            model = joblib.load("logreg")
            prediction = model.predict([features])
            st.markdown(f"Prediction:{prediction}")
            
            if prediction == 1:
                st.markdown("Flood Will Occur.")
            elif prediction == 0:
                st.markdown("Flood will not Occur.")

with dataset:
    data = pd.read_csv("dataset.csv")
    data = st.dataframe(data)

with about:
    st.markdown(":red[Name:] HAPPINESS OLATUNDE")