from dis import code_info
import streamlit as st
import joblib
import numpy as np
import pandas as pd
from hinselmann import hinselmann_model
from schiller import schiller_model
from citology import citology_model
from biopsy import biopsy_model

def user_input():

    st.header('Cervical Cancer Detection Page')

    st.subheader('Information collected from respondents is kept ***strictly confidential***.')
    st.write('We do not collect your information, nor your test result.')

    age = st.number_input('Enter your age')
    
    sexual_partner = st.slider('How many sexual partners have you had?', 0, 20)

    first_intercourse = st.number_input('When was your first sexual intercourse (age)?')

    pregnancy = st.slider('How many times have you been pregnant?', 0, 10)

    hmc = st.selectbox('Have you used Hormonal Contraceptive?', ['No', 'Yes'])

    if hmc == 'Yes':
        hmc = 1
        hmc_year = st.number_input('If yes, how long have you used hormonal contraceptive (year)?')
    else:
        hmc = 0
        hmc_year = 0

    IUD = st.selectbox('Have you used IUD?', ['No', 'Yes'])
    if IUD == 'Yes':
        IUD = 1
    else:
        IUD = 0

    cancer = st.selectbox('Have you had any type of cancer?', ['No', 'Yes'])
    if cancer == 'Yes':
        cancer = 1
    else:
        cancer = 0


    hinselmann = np.array([age, sexual_partner, first_intercourse, pregnancy, hmc, hmc_year, IUD, cancer]).reshape(1, 8)
    schiller = np.array([age, sexual_partner, first_intercourse, pregnancy, hmc, hmc_year, IUD]).reshape(1, 7)
    citology = np.array([age, sexual_partner, first_intercourse, pregnancy, hmc, hmc_year]).reshape(1, 6)
    biopsy = np.array([age, sexual_partner, first_intercourse, pregnancy, hmc, hmc_year, IUD, cancer]).reshape(1, 8)

    return {'hinselmann': hinselmann, 'schiller': schiller, 'citology': citology, 'biopsy': biopsy}

def check_cancer(result):
    count = 0
    for i in result:
        if i == 'Positive':
            count += 1
    
    if count == 1:
        return '1/4 tests predicts that you are at risk of having cervical cancer.'
    elif count > 1:
        return f'{count}/4 tests predict that you are at risk of having cervical cancer.'

    return 'You are predictedly negative with cervical cancer. Please have regular check-ups.'

def show_predict_page():

    st.sidebar.title("Cervical Cancer Detection")

    st.sidebar.write("""### We need some information to predict your cervical health status""")

    info = user_input()
    st.write(pd.DataFrame(info['hinselmann'],columns=['Age','Number of sexual partners',
       'First sexual intercourse', 'Num of pregnancies','Hormonal Contraceptives',
       'Hormonal Contraceptives (years)', 'IUD','Dx:Cancer']))

    if st.button("Predict"):
        # hinselmann_test
        model_hinselmann = hinselmann_model()
        prediction_hinselmann = model_hinselmann.predict(info['hinselmann'])
        if prediction_hinselmann == np.array([0]):
            prediction_hinselmann = 'Negative'
        else: 
            prediction_hinselmann = 'Positive'
        # st.subheader(f"Your Hinselmann test predicted result is: {prediction_hinselmann}")

        # schiller_test
        model_schiller = schiller_model()
        prediction_schiller = model_schiller.predict(info['schiller'])
        if prediction_schiller == np.array([0]):
            prediction_schiller = 'Negative'
        else: 
            prediction_schiller = 'Positive'
        # st.subheader(f"Your Schiller test predicted result is: {prediction_hinselmann}")

        # citology_test
        model_citology = citology_model()
        prediction_citology = model_citology.predict(info['citology'])
        if prediction_citology == np.array([0]):
            prediction_citology = 'Negative'
        else: 
            prediction_citology = 'Positive'
        # st.subheader(f"Your Citology test predicted result is: {prediction_hinselmann}")
        
        # biopsy_test
        model_biopsy = biopsy_model()
        prediction_biopsy = model_biopsy.predict(info['biopsy'])
        if prediction_biopsy == np.array([0]):
            prediction_biopsy = 'Negative'
        else: 
            prediction_biopsy = 'Positive'
        # st.subheader(f"Your Biopsy test predicted result is: {prediction_hinselmann}")


        result_collection = np.array([prediction_hinselmann, prediction_schiller, 
                                prediction_citology, prediction_biopsy])
        result = pd.DataFrame(result_collection.reshape(1,4),
                                columns=['Hinselmann test', 'Schiller test', 'Citology test', 'Biopsy test'],index=['Result'])
        
        st.table(result)

        st.header(check_cancer(result_collection))

if __name__ == "__main__":
    show_predict_page()