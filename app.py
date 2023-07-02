import streamlit as st
import pickle

pipe = pickle.load(open('pipe.pkl','rb'))

teams=['Australia',
    'India',
    'Bangladesh',
    'New Zealand',
    'South Africa',
    'England',
    'West Indies',
    'Afghanistan',
    'Pakistan',
    'Sri Lanka'
       ]
cities = ['Colombo',
 'Mirpur',
 'Johannesburg',
 'Dubai',
 'Auckland',
 'Cape Town',
 'London',
 'Pallekele',
 'Barbados',
 'Melbourne',
 'Durban',
 'St Lucia',
 'Wellington',
 'Sydney',
 'Lauderhill',
 'Hamilton',
 'Centurion',
 'Abu Dhabi',
 'Manchester',
 'Mumbai',
 'Nottingham',
 'Southampton',
 'Mount Maunganui',
 'Chittagong',
 'Kolkata',
 'Lahore',
 'Delhi',
 'Nagpur',
 'Cardiff',
 'Chandigarh',
 'Adelaide',
 'Bangalore',
 'St Kitts',
 'Christchurch',
 'Trinidad']

st.title('Cricket Score Predictor')
col1, col2= st.beta_columns(2)

with col1:
  batting_team= st.selectbox('Select batting team', sorted(teams))
with col2:
  bowling_team= st.selectbox('Select bowling team', sorted(teams))

city = st.selectbox('Select City',sorted(cities))

col3,col4,col5= st.beat_columns(3)
with col3:
  current_score= st.number_input('current Score')
with col4:
  overs= st.number_input('Overs done(Must be above 5)')
with col5:
  wickets= st.number_input('wickets out')

last_five = st.number_input('Runs scored in last 5 overs')

if st.button('Predict Score'):
  pass