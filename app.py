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
    with st.form(key="flood",):
        #Rainfall	Max Temperature	Min Temperature	Relative Humidity	Flood
        rainfall = st.text_input("RainFall ")
        max_tem = st.text_input("Max Temperature ")
        min_tem = st.text_input("Min Temperature")
        rel_hum = st.text_input("Relative Humidity")
        submit = st.form_submit_button("Predict💧",type="primary")

        if rainfall or max_tem or min_tem or rel_hum != '':
            if submit:
                    #list
                features = [float(rainfall),float(max_tem),float(min_tem),float(rel_hum)]
                model = joblib.load("logreg")
                prediction = model.predict([features])
                
                if prediction == 1:
                    st.markdown(f"Predicted Value: 1")
                    st.markdown(":red[Flood Will Occur].")
                elif prediction == 0:
                    st.markdown(f"Predicted Value: 0")
                    st.markdown("Flood will not Occur.")
        else:
            st.error("Empty inputs may result to errors.",icon="🚨")

with dataset:
    #dataset
    st.write(':red[Flood Dataset]')
    data = pd.read_csv("dataset.csv")
    data = st.dataframe(data)
    #algorithm used
    st.write('### Source: :red[ NiMet]')


with about:
    st.markdown(":red[Name:] OLATUNDE IYABO HAPPINESS")
    st.markdown(":red[School:] FEDERAL UNIVERSITY LOKOJA")
    st.markdown(":red[Strength:] Team Work")
    st.markdown(":red[I am passionate about learning new things.] ")