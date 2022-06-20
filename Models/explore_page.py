import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def show_explore_page():
    st.markdown("## What is Cervical Cancel?")
    st.markdown("""
    ### Cervical cancer is the fourth most common cancer in women compared to other types of cancer. However, you can protect your self by early detecting this disease.""")

    st.write('')

    with st.container():
        image_col, text_col = st.columns((1,1))
        with image_col:
            st.image("https://www.quellerfisher.com/blog/wp-content/uploads/sites/464/2018/02/Cervical-cancer-simple-illustration.jpg")
            st.markdown("""
            [Fig. 1.](https://www.quellerfisher.com/blog/wp-content/uploads/sites/464/2018/02/Cervical-cancer-simple-illustration.jpg) Cervical Cancer illustration""")

        with text_col:
            st.subheader("Overview of Cervical Cancer")
            st.write("""Cervical cancer is a type of cancer in which abnormal cell growth occurs in the cervix, the lower part of the uterus. 
            The cervix connects the uterus to the vagina. The figure depicts a cervix with abnormal cell growth developing into a tumor
            Cervical cancer is the fourth most common cancer in women compared to other types of cancer, with an estimated 604 000 new cases and 342 000 deaths in 2020. 
            About 90% of the new cases and deaths worldwide in 2020 occurred in low- and middle-income countries.""")
            st.markdown("[Read more...](https://www.cdc.gov/cancer/cervical/basic_info/)")

    
    st.markdown("##")
    st.markdown("## How this model works?")
 
    st.markdown("""
    Early detection of cervical cancer is crucial to reduce this disease's deadliness. 
    Several predictive models are built based on data collected from 858 women from [UCI Machine Learning Repository](https://archive-beta.ics.uci.edu/ml/datasets/cervical+cancer+risk+factors) with 32 features and 4 targets, which are also the 4 most common tests for cervical cancer: Hinselmann, Schiller, Cytology, and Biopsy. 
    
    This dataset suffers from imbalance with only less than 9% positive patients and approximately 20% missing values. Besides, 32 attributes appear redundant to feed a predictive model, which may lead to potential overfitting. Therefore, several machine learning approaches have been deployed to deal with the aforementioned problems, such as feature engineering, resampling, and feature selection. The developer found that GridSearchCV Classification, with the support of Border-SMOTE and Meta-transformer for selecting features based on importance weights for the Hinselmann, shows the most outstanding performance, with 9 chosen features, generating an accuracy of 98.18%.""")

    st.markdown('')

    st.write('Table 1. Models with best performance for each target')
    
    st.markdown("""
| Test       |                        Model                        | No of Features | Accuracy | Precision | Sensitivity | Specificity |   F-1  |
|------------|:---------------------------------------------------:|:--------------:|:--------:|:---------:|:-----------:|:-----------:|:------:|
| Hinselmann | Grid Search CV + Borderline-SMOTE + SelectFromModel |        8       |  98.18%  |   98.76%  |    97.55%   |    98.80%   | 98.15% |
|  Schiller  |  Random Forest + Borderline-SMOTE + SelectFromModel |        7       |  96.17%  |   96.58%  |    95.27%   |    96.97%   | 95.92% |
|  Citology  | Grid Search CV + Borderline-SMOTE + SelectFromModel |        6       |  97.54%  |   97.65%  |    97.65%   |    97.42%   | 96.74% |
|   Biopsy   |  Random Forest + Borderline-SMOTE + SelectFromModel |        8       |  96.57%  |  100.00%  |    93.13%   |   100.00%   | 96.44% |
    
    """)

    st.markdown('')
    st.markdown("## What Are the Risk Factors for Cervical Cancer?")

    st.markdown("""There are several factor that may increase your chance of having cervical cancer. Each test mentioned above weights each factor differently. However, they all come to consensus with 8 most important risk factors, which are asked in the predict page:""")
    
    st.markdown('   *  1. Age')
    st.markdown('   *  2. Number of sexual partners')
    st.markdown('   *  3. First sexual intercourse') 
    st.markdown('   *  4. Number of pregnancies')    
    st.markdown('   *  5. Use of hormonal contraceptives')    
    st.markdown('   *  6. Duration of hormonal contraceptives usage')    
    st.markdown('   *  7. Use of IUD')    
    st.markdown('   *  8. Presense of other types of cancer')    

    st.markdown('')
    # st.image("Feature Importances - Hinselmann.png", caption='Feature Importances - Hinselmann Test')
    # st.markdown('')
    # st.image("Feature Importances - Schiller.png", caption='Feature Importances - Schiller Test')
    # st.markdown('')
    # st.image("Feature Importances - Citology.png", caption='Feature Importances - Citology Test')
    # st.markdown('')
    # st.image("Feature Importances - Biopsy.png", caption='Feature Importances - Biopsy Test')

    with st.container():
        image1, image2 = st.columns((1,1))
        with image1:
            st.image("https://scontent-ort2-1.xx.fbcdn.net/v/t39.30808-6/289427117_1157939874938728_5142108399346703256_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=730e14&_nc_ohc=XcRilQctbN8AX_8c58A&tn=pP2okOx80sPGDgTM&_nc_ht=scontent-ort2-1.xx&oh=00_AT_-jxKAWqIVylOhUSZiIEdygvWZr9WVFpttJXP9imnPyQ&oe=62B4BB5B", caption='Fig. 2. Feature Importances - Hinselmann Test')
        with image2:
            st.image("https://scontent-ort2-1.xx.fbcdn.net/v/t39.30808-6/289285787_1157939858272063_2451351868148193044_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=730e14&_nc_ohc=jKlWEfvhlosAX8AaPPm&_nc_ht=scontent-ort2-1.xx&oh=00_AT8Hg843oVK2muBqyc66YBuiGXaRlDk3ntkOWegXvp_mWQ&oe=62B5AA43", caption='Fig. 3. Feature Importances - Schiller Test')

    with st.container():
        image1, image2 = st.columns((1,1))
        with image1:
            st.image("https://scontent-ort2-1.xx.fbcdn.net/v/t39.30808-6/289344790_1157939864938729_5397285092162796601_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=730e14&_nc_ohc=SilmKlWKiusAX8Qymyz&tn=pP2okOx80sPGDgTM&_nc_ht=scontent-ort2-1.xx&oh=00_AT-cUO_Ktj6sKFse8a2JGsovoPfXtdGu-86K8znjk_MBFw&oe=62B56702", caption='Fig. 4. Feature Importances - Citology Test')
        with image2:
            st.image("https://scontent-ort2-1.xx.fbcdn.net/v/t39.30808-6/289295916_1157939861605396_8182708816788922842_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=730e14&_nc_ohc=Gefp71s1K8gAX8FrAww&tn=pP2okOx80sPGDgTM&_nc_ht=scontent-ort2-1.xx&oh=00_AT_qsToD-peR_9U_uUHCZ3Ww0BUA_p9pBMuCPAks9EQ_WQ&oe=62B3ED34", caption='Fig. 5. Feature Importances - Biopsy Test')

    
    
    
    
    
    
    
    
    
    
    
    
