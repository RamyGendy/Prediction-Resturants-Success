import streamlit as st
import numpy as np
import pandas as pd
import joblib

model= joblib.load('final_model_1.sav')

columns= ['online_order', 'book_table', 'votes', 'average_cost', 'meal_type','neighborhood', 'rest_type_count', 'cuisines_total']

st.markdown( '''
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://wallpapercave.com/wp/wp10509755.jpg");
background-size: cover;
}
[data-testid="stHeader"] {
background: rgba(0,0,0,0);
}
</style>''', unsafe_allow_html=True)

st.title('How your restaurant will success in Bangalore? :convenience_store:')

online_order= st.radio("Do you offer online ordering option in the resturant?",['Yes', 'No'])

book_table= st.radio("Do you offer Booking tables option in th resturant?",['Yes', 'No'])

votes= st.slider('how many votes the resturant have?',
                 min_value=0, max_value=16832, value=0, step=50)

average_cost= st.slider('how much on average you want a two persons to spend?',
                        min_value=50, max_value=6000, value=50, step=50)

meal_type= st.selectbox('what type of the resturant', 
                        ['Buffet', 'Cafes', 'Delivery', 'Desserts', 'Dine-out', 'Drinks & nightlife', 'Pubs and bars'])

neighborhood= st.selectbox('Where you will start your restaurant?',
                           ['Banashankari', 'Bannerghatta Road', 'Basavanagudi', 'Bellandur',
                            'Brigade Road', 'Brookefield', 'BTM', 'Church Street',
                            'Electronic City', 'Frazer Town', 'HSR', 'Indiranagar',
                            'Jayanagar', 'JP Nagar', 'Kalyan Nagar', 'Kammanahalli',
                            'Koramangala 4th Block', 'Koramangala 5th Block',
                            'Koramangala 6th Block', 'Koramangala 7th Block', 'Lavelle Road',
                            'Malleshwaram', 'Marathahalli', 'MG Road', 'New BEL Road',
                            'Old Airport Road', 'Rajajinagar', 'Residency Road',
                            'Sarjapur Road', 'Whitefield'])

rest_type_count= st.select_slider('how many area the resturant serveing',[1, 2])

cuisines_total= st.select_slider('how many cuisines the resturant serveing',[1, 2, 3, 4, 5, 6, 7, 8])

m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #d17f62;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #e2af9d;
    color:#ff0000;
    }
</style>""", unsafe_allow_html=True)

if st.button('Predict Success Rate'):
    col= np.array([online_order, book_table, votes, average_cost, meal_type, neighborhood, rest_type_count, cuisines_total])
    data= pd.DataFrame([col], columns=columns)
    prediction= model.predict(data)[0]

    if prediction == 1:
        st.success('High Success Rate :thumbsup:')
    else:
        st.error('Low Success Rate :thumbsdown:')
