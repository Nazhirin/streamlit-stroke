import pickle
import streamlit as st

# membaca model
dataset_model = pickle.load(open('stroke_model1.sav', 'rb'))

#judul web
st.title('Prediksi Stroke')
#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    id = st.text_input ('id')

with col1 :
    gender = st.text_input ('gender')

with col1 :
    age = st.text_input ('age')

with col1 :
    hypertension  = st.text_input ('hypertension')

with col1 :
    heart_disease = st.text_input ('heart_disease')

with col1 :
    ever_married = st.text_input ('ever_married')

with col1 :
    work_type = st.text_input ('work_type')

with col1 :
    Residence_type = st.text_input ('Residence_type')

with col1 :
    avg_glucose_level = st.text_input ('avg_glucose_level')

with col1 :
    bmi = st.text_input ('bmi')

with col1 :
    smoking_status = st.text_input ('smoking_status')

# code untuk prediksi
heart_diangnosis = ''

# membuat tombol untuk prediksi
if st.button('test predict') :
    heart_prediction = dataset_model.predict([[id,gender,age,hypertension,heart_disease,ever_married,work_type,Residence_type,avg_glucose_level,bmi,smoking_status]])

    if(heart_prediction[0] == 1):
        heart_diangnosis = 'berpotensi stroke'
    else :
        heart_diangnosis = 'tidak berpotensi stroke'
    
    st.success(heart_diangnosis)