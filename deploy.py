import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image
  
# loading in the model to predict on the data
pickle_in = open('Lclassifier.pkl', 'rb')
classifier = pickle.load(pickle_in)
  
def welcome():
    return 'Early Detection and Classification of Coronary Artery Disease (CAD) using Machine Learning Models'
  
# defining the function which will make the prediction using 
# the data which the user inputs
def prediction(age, sex_input, chest_pain_type_input, rest_blood_press, cholesterol, fasting_blood_sugar_input, rest_ecg_input, 
            max_heart_rate_input, exer_ind_angina_input, st_depression, st_slope_input, num_major_vessels, thallium_scint_input):  
   
    prediction = classifier.predict(
        [[age, sex_input, chest_pain_type_input, rest_blood_press, cholesterol, fasting_blood_sugar_input, rest_ecg_input, 
            max_heart_rate_input, exer_ind_angina_input, st_depression, st_slope_input, num_major_vessels, thallium_scint_input]])
    print(prediction)
    return prediction
      
  
# this is the main function in which we define our webpage 
def main():
      # giving the webpage a title
    st.title("Early Detection and Classification of Coronary Artery Disease")
      
    # here we define some of the front end elements of the web page like 
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:blue;padding:13px">
    <h2 style ="color:black;text-align:center;">Early Detection and Classification of Coronary Artery Disease ML App </h2>
    </div>
    """
      
    # this line allows us to display the front end aspects we have 
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
    
    # the following lines create text boxes in which the user can enter 
    # the data required to make the prediction
    age_input = st.text_input("Age")
    age = float(age_input) if age_input else 0.0 
    def preprocess_input(sex):
        if sex.upper() == 'FEMALE':
            sex1 = 0
        else:
            sex1 = 1 
        return sex1
    sex = st.text_input("Sex")
    sex_input = preprocess_input(sex)

    def preprocess_chest(chest_pain_type):
        if chest_pain_type.upper() == 'TYPICAL ANGINA':
            chest_pain_type1 = 1
        elif chest_pain_type.upper() == 'ATYPICAL ANGINA':
            chest_pain_type1 = 2
        elif chest_pain_type.upper() == 'NONANGINA PAIN':
            chest_pain_type1 = 3
        else:
         chest_pain_type1 = 4
        return  chest_pain_type1
    chest_pain_type = st.text_input("Chest pain type")
    chest_pain_type_input = preprocess_chest(chest_pain_type)

    rest_blood_press_input = st.text_input("Rest Blood Pressure")
    rest_blood_press = float(rest_blood_press_input) if rest_blood_press_input else 0.0 

    cholesterol_input = st.text_input("Cholesterol")
    cholesterol = float(cholesterol_input) if cholesterol_input else 0.0 

    fasting_blood_sugar = st.text_input("Fasting Blood Sugar")
    def preprocess_sugar(fasting_blood_sugar):
        if fasting_blood_sugar.upper() == 'TRUE':
            fasting_blood_sugar1 = 1
        else:
            fasting_blood_sugar1 = 0 
        return fasting_blood_sugar1
    fasting_blood_sugar_input = preprocess_sugar(fasting_blood_sugar)
    
    rest_ecg = st.text_input("Rest Electrocardiogram")
    def preprocess_sugar(rest_ecg):
        if rest_ecg.upper() == 'NORMAL':
            rest_ecg1 = 0
        elif rest_ecg.upper() == 'HAVING ST-T WAVE ABNORMAL':
            rest_ecg1 = 1 
        else: 
            rest_ecg1 = 2
        return rest_ecg1
    rest_ecg_input =preprocess_sugar(rest_ecg)

    max_heart_rate = st.text_input("Maximum Heart Rate")
    max_heart_rate_input = float(max_heart_rate) if max_heart_rate else 0.0 

    exer_ind_angina = st.text_input("Exertional angina")
    def preprocess_heart(exer_ind_angina):
        if exer_ind_angina.upper() == 'NO':
            exer_ind_angina1 = 0
        else:
            exer_ind_angina1= 1 
        return exer_ind_angina1
    exer_ind_angina_input = preprocess_heart(exer_ind_angina)

    st_depression_input = st.text_input("ST Depression")
    st_depression = float(st_depression_input) if st_depression_input else 0.0 

    st_slope = st.text_input("ST Slope")
    def preprocess_st_slope(st_slope):
        if st_slope.upper() == 'UNSLOPING':
            st_slope1 = 1
        elif st_slope.upper() == 'FLAT':
            st_slope1 = 2 
        else: 
            st_slope1 = 3
        return st_slope1       
    st_slope_input = preprocess_st_slope(st_slope)     

    num_major_vessels_input = st.text_input("Number of major blood vessels")
    num_major_vessels = float(num_major_vessels_input) if num_major_vessels_input else 0.0 

    thallium_scint = st.text_input("Thallium scintigraphy")
    def preprocess_thallium_scint(thallium_scint):
        if thallium_scint.upper() == 'FIXED':
            thallium_scint1 = 6
        elif thallium_scint.upper() == 'NORMAL':
            thallium_scint1 = 3 
        else:
            thallium_scint1 = 7
        return thallium_scint1
    thallium_scint_input = preprocess_thallium_scint(thallium_scint)


    result =""
      
    def get_disease_name(prediction):
        if prediction == 0:
            disease_name = "No Disease"
        elif prediction == 1:
            disease_name = "  Coronary Artery Disease (CAD)"
        return disease_name
    
    disease_name = "Unknown"  # Default value
    # the below line ensures that when the button called 'Predict' is clicked, 
    # the prediction function defined above is called to make the prediction 
    # and store it in the variable result
    if st.button("Predict"):
        result = prediction(age, sex_input, chest_pain_type_input, rest_blood_press, cholesterol, fasting_blood_sugar_input, rest_ecg_input, 
            max_heart_rate_input, exer_ind_angina_input, st_depression, st_slope_input, num_major_vessels, thallium_scint_input)
        disease_name = get_disease_name(result)
    st.success('You have {}'.format(disease_name))
     
if __name__=='__main__':
    main()