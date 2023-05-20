import streamlit as st

import numpy as np
import pandas as pd
import joblib

model= joblib.load('final_model.joblip')

st.title('How your restaurant will success in Bangalore?')

online_order= st.selectbox('online order option in the resturant?',('Yes','No'))
book_table= st.selectbox('Book table option in th resturant?',('Yes','No'))
votes= st.number_input('how many votes the resturant have?',0)
average_cost= st.number_input('how much on average you want a two persons to spend?',0)
meal_type= st.selectbox('what type of the resturant',('Buffet','Cafes','Delivery','Desserts',
                                                 'Bars','Drinks & nightlife','Dine_out'))
neighborhood= st.selectbox('Where you will start your restaurant?',
('Banashankari', 'Bannerghatta Road', 'Basavanagudi', 'Bellandur',
       'Brigade Road', 'Brookefield', 'BTM', 'Church Street',
       'Electronic City', 'Frazer Town', 'HSR', 'Indiranagar',
       'Jayanagar', 'JP Nagar', 'Kalyan Nagar', 'Kammanahalli',
       'Koramangala 4th Block', 'Koramangala 5th Block',
       'Koramangala 6th Block', 'Koramangala 7th Block', 'Lavelle Road',
       'Malleshwaram', 'Marathahalli', 'MG Road', 'New BEL Road',
       'Old Airport Road', 'Rajajinagar', 'Residency Road',
       'Sarjapur Road', 'Whitefield'))
rest_type_count= st.select_slider('how many area the resturant serveing',[1,2])
cuisines_total= st.select_slider('how many cuisines the resturant serveing',[1,2,3,4,5,6,7,8])


columns= ['online_order', 'book_table', 'votes', 'average_cost', 'meal_type',
          'neighborhood', 'rest_type_count', 'cuisines_total']



def predict():
    col= np.array(['online_order', 'book_table', 'votes', 'average_cost', 'meal_type','neighborhood', 'rest_type_count', 'cuisines_total'])
    data= pd.DataFrame([col], columns=columns)
    prediction= model.predict(data)[0]

    if prediction == 1:
        st.success('High Success Rate :thumbsup:')
    else:
        st.error('Low Success Rate:thumbsdown:')





m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #0099ff;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #00ff00;
    color:#ff0000;
    }
</style>""", unsafe_allow_html=True)

st.button('Predict', on_click=predict)





