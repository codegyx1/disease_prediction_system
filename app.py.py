import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="PREDICTION OF DISEASES OUTBREAK", layout="wide", 
                   page_icon="doctor")
Diabetes_model = pickle.load(open(r"C:\Users\Hp\Desktop\python project\dia_prediction.sav","rb"))
paekinsos_model = pickle.load(open(r"C:\Users\Hp\Desktop\python project\parkinsons_prediction.sav","rb"))
heart_model = pickle.load(open(r"C:\Users\Hp\Desktop\python project\heart_prediction.sav","rb"))

with st.sidebar:
    selected = option_menu("Prediction of disease outbreak sytem",
                         ["Diabetes disease prediction", "parkinsons disease prediction", "heart disease prediction"],
                         menu_icon="hospital-fill", 
                         icons=["activity", "heart", "person"],
                         default_index=0)

if selected == "Diabetes disease prediction":
    st.title("Diabetes prdiction using ML")
    col1,col2,col3 = st.columns(3)
    with col1:
        pregnacies=st.text_input("Number of pregnancies")
    with col2:
        glucose=st.text_input("Glucose level")
    with col3:
        bloodpressure=st.text_input("Blood pressure value")
    with col1:
        skinthickness=st.text_input("Skin thickness value")
    with col2:
        insulin=st.text_input("Insulin level")
    with col3:
        bmi=st.text_input("Body mass index")
    with col1:
        diabetespedigreefunction=st.text_input("Diabetes pedigree function value")
    with col2:
        age=st.text_input("Age of the person")
    
    diabetes_diagnosis = ""
    if st.button("Diabetes test result"):
        user_input = [[pregnacies,glucose,bloodpressure,skinthickness,insulin,bmi,diabetespedigreefunction,age]]
        diabetes_prediction = Diabetes_model.predict([[pregnacies,glucose,bloodpressure,skinthickness,insulin,bmi,diabetespedigreefunction,age]])
        if(diabetes_prediction[0]==1):
            diabetes_diagnosis = "The person is diabetic"
        else:
            diabetes_diagnosis = "The person is not diabetic"
    st.success(diabetes_diagnosis)

if selected == "parkinsons disease prediction":
    st.title("parkinsons disease prediction using ML")
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        fo=st.text_input("MDVP:Fo(Hz)")
    with col2:
        fhi=st.text_input("MDVP:Fhi(Hz)")
    with col3:
        flo=st.text_input("MDVP:Flo(Hz)")
    with col4: 
        Jitter_percent=st.text_input("Jitter:percent")
    with col5:
        Jitter_Abs=st.text_input("Jitter:Abs")
    with col1:
        RAP=st.text_input("MDVP:RAP")
    with col2:
        PPQ=st.text_input("MDVP:PPQ")
    with col3:
        DDP=st.text_input("Jitter:DDP")
    with col4:
        Shimmer=st.text_input("MDVP:Shimmer")
    with col5:
        Shimmer_dB=st.text_input("MDVP:Shimmer(dB)")
    with col1:
        APQ3=st.text_input("Jitter:APQ3")
    with col2:
        APQ5=st.text_input("Jitter:APQ5")
    with col3:
        APQ=st.text_input("Jitter:APQ")
    with col4:
        DDA=st.text_input("Jitter:DDA")
    with col5:
        NHR=st.text_input("Jitter:NHR")
    with col1:
        HNR=st.text_input("Jitter:HNR")
    with col2:
        RPDE=st.text_input("Jitter:RPDE")
    with col3:
        DFA=st.text_input("Jitter:DFA")
    with col4:
        spread1=st.text_input("Jitter:spread1")
    with col5:
        spread2=st.text_input("Jitter:spread2")
    with col1:
        D2=st.text_input("Jitter:D2")
    with col2:
        PPE=st.text_input("Jitter:PPE")
    
    parkinsons_diagnosis = ""
    if st.button("parkinsons test result"):
        user_input = [[fo,fhi,flo,Jitter_percent,Jitter_Abs,RAP,PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]]
        parkinsons_prediction = paekinsos_model.predict(user_input)
        if(parkinsons_prediction[0]==1):
            parkinsons_diagnosis = "The person is parkinsons"
        else:
            parkinsons_diagnosis = "The person is not parkinsons"
    st.success(parkinsons_diagnosis)    

if selected == "heart disease prediction":
    st.title("heart disease prediction using ML")
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        age=st.text_input("Age") 
    with col2:
        sex=st.text_input("Sex")
    with col3:
        cp=st.text_input("Chest pain type")
    with col4:
        trestbps=st.text_input("Resting blood pressure")        
    with col5:
        chol=st.text_input("Serum cholestoral in mg/dl")
    with col1:
        fbs=st.text_input("Fasting blood sugar > 120 mg/dl")
    with col2:
        restecg=st.text_input("Resting electrocardiographic results")
    with col3:
        thalach=st.text_input("Maximum heart rate achieved")
    with col4:
        exang=st.text_input("Exercise induced angina")
    with col5:
        oldpeak=st.text_input("ST depression induced by exercise relative to rest")
    with col1:
        slope=st.text_input("Slope of the peak exercise ST segment")
    with col2:
        ca=st.text_input("Major vessels colored by flourosopy")
    with col3:
        thal=st.text_input("thal: 0 = normal; 1 = fixed defect; 2 = reversable defect")
        
    heart_diagnosis = ""
    if st.button("heart disease test result"):
        user_input = [[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]]
        heart_prediction = heart_model.predict(user_input)
        if(heart_prediction[0]==1):
            heart_diagnosis = "The person is having heart disease"  
        else:
            heart_diagnosis = "The person is not having heart disease"
    st.success(heart_diagnosis)
    

        
        



