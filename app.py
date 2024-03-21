import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models
diabetes_model = pickle.load(open('models/diabetes.sav', 'rb'))
heart_disease_model = pickle.load(open('models/HeartDisease.sav', 'rb'))
parkinsons_model = pickle.load(open('models/parkinsons.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction Web Application',
                           ['About', 'Diabetes Prediction', 'Heart Disease Prediction',
                            'Parkinsons Disease Prediction'],
                           icons=['person-circle', 'activity', 'heart', 'person'],
                           default_index=0)

# About Page
if (selected == 'About'):
    # page title
    st.title('About')
    st.text('This is a Multiple Disease Prediction Web Application which uses machine learning.')
    st.text('Use the Tabs to select which disease needs to be detected.')
    st.text('Thereafter input the relevant information of the patient and click the')
    st.text('Test Result button at the bottom of the page.')
    st.text('Only numerical values will be accepted')

# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    # page title
    st.title('Diabetes Prediction')

    # getting input data from user
    # columns for input fields
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col4:
        SkinThickness = st.text_input('Skin Thickness value')
    with col1:
        Insulin = st.text_input('Insulin Level')
    with col2:
        BMI = st.text_input('BMI value')
    with col3:
        Diabetes_Pedigree_Function = st.text_input('Pedigree Function value')
    with col4:
        Age = st.text_input('Age of the Person')

    # code for prediction
    diabetes_diagnoses = ''

    # creating button for prediction
    if st.button('Diabetes Test Result'):
        diabetes_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, Diabetes_Pedigree_Function, Age]])
        if diabetes_prediction[0] == 1:
            diabetes_diagnoses = 'The person is Diabetic'
        else:
            diabetes_diagnoses = 'The person in not Diabetic'
        st.success(diabetes_diagnoses)







# Heart Disease Prediction
if (selected == 'Heart Disease Prediction'):
    # page title
    st.title('Heart Disease Prediction')

    # getting input data from user
    # columns for input fields
    col1, col2, col3, col4 = st.columns(4)



    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('sex')
    with col3:
        cp = st.text_input('cp')
    with col4:
        trestbps = st.text_input('trestbps')
    with col1:
        chol = st.text_input('chol')
    with col2:
        fbs = st.text_input('fbs')
    with col3:
        restecg = st.text_input('restecg')
    with col4:
        thalach = st.text_input('thalach')
    with col1:
        exang = st.text_input('exang')
    with col2:
        oldpeak = st.text_input('oldpeak')
    with col3:
        slope = st.text_input('slope')
    with col4:
        ca = st.text_input('ca')
    with col1:
        thal = st.text_input('thal')


    # code for prediction
    heart_disease_diagnosis = ''

    # creating button for prediction
    if st.button('Heart Disease Test Result'):
        heart_disease_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        if heart_disease_prediction[0] == 1:
            heart_disease_diagnosis = 'The person is Diabetic'
        else:
            heart_disease_diagnosis = 'The person in not Diabetic'
        st.success(heart_disease_diagnosis)


# Parkinsons Disease Prediction
if (selected == 'Parkinsons Disease Prediction'):
    # page title
    st.title('Parkinsons Disease Prediction')

    # getting input data from user
    # columns for input fields
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        MDVPFo = st.text_input('MDVP: Fo(Hz)')
    with col2:
        MDVPFhi = st.text_input('MDVP')
    with col3:
        MDVPFlo = st.text_input('MDVP: Flo(Hz)')
    with col4:
        MDVPJitter = st.text_input('MDVP: Jitter(%)')
    with col1:
        MDVPJitter = st.text_input('MDVP: Jitter(Abs)')
    with col2:
        MDVPRAP = st.text_input('MDVP: RAP')
    with col3:
        MDVPPPQ = st.text_input('MDVP: PPQ')
    with col4:
        JitterDDP = st.text_input('Jitter: DDP')
    with col1:
        MDVPShimmer = st.text_input('MDVP: Shimmer')
    with col2:
        MDVPShimmer = st.text_input('MDVP: Shimmer(dB)')
    with col3:
        ShimmerAPQ3 = st.text_input('Shimmer: APQ3')
    with col4:
        ShimmerAPQ5 = st.text_input('Shimmer: APQ5')
    with col1:
        MDVPAPQ = st.text_input('MDVP: APQ')
    with col2:
         ShimmerDDA = st.text_input('Shimmer: DDA')
    with col3:
         NHR = st.text_input('NHR')
    with col4:
         HNR = st.text_input('HNR')
    with col1:
         RPDE = st.text_input('RPDE')
    with col2:
         DFA = st.text_input('DFA')
    with col3:
         spread1 = st.text_input('spread1')
    with col4:
         spread2 = st.text_input('spread2')
    with col1:
         D2 = st.text_input('D2')
    with col2:
         PPE = st.text_input('PPE')

    # code for prediction
    diabetes_diagnoses = ''

    # creating button for prediction
    if st.button('Diabetes Test Result'):
        diabetes_prediction = diabetes_model.predict([[MDVPFo, MDVPFhi, MDVPFlo,
                                                    MDVPJitter, MDVPJitter, MDVPRAP, MDVPPPQ, JitterDDP,
                                                    MDVPShimmer, MDVPShimmer, ShimmerAPQ3, ShimmerAPQ5, MDVPAPQ,
                                                    ShimmerDDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])

        if diabetes_prediction[0] == 1:
            diabetes_diagnoses = 'The person is Diabetic'
        else:
            diabetes_diagnoses = 'The person in not Diabetic'
        st.success(diabetes_diagnoses)