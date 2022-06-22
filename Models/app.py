import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

lan = st.sidebar.selectbox("Choose language", ['English', 'Tiếng Việt'])
page = st.sidebar.selectbox("Explore or Predict", ('Predict', 'Explore'))
st.sidebar.write('For any concerns or inquiries, contact developer at ngoa@berea.edu')

if lan == 'Tiếng Việt':
    lan = 'vn'
else:
    lan = 'en'
    
if page == 'Predict':
    show_predict_page(lan)
else:
    show_explore_page()

