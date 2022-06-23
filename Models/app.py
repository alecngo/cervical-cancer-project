import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

texts = {   'select': {        
                'en': "Explore or Predict",
                'vn': "Khám phá hay dự đoán"
            },
            'concern': {
                'en': 'For any concerns or inquiries, contact developer at ngoa@berea.edu',
                'vn': 'Nếu có bất kỳ thắc mắc hay yêu cầu nào, vui lòng liên hệ developer tại ngoa@berea.edu'
            },
            'predict': {
                'en': 'Predict',
                'vn': 'Dự đoán'
            },
            'explore': {
                'en': 'Explore',
                'vn': 'Khám phá'
            }
}   

lan = st.sidebar.selectbox("Choose language", ['English', 'Tiếng Việt'])

if lan == 'Tiếng Việt':
    lan = 'vn'
else:
    lan = 'en'

def main(lan):

    page = st.sidebar.selectbox(texts['select'][lan], (texts['predict'][lan], texts['explore'][lan]))
    st.sidebar.write(texts['concern'][lan])

    if page == texts['predict'][lan]:
        show_predict_page(lan)
    else:
        show_explore_page(lan)

