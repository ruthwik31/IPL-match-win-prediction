import streamlit as st
import pickle
import sklearn
import pandas as pd


teams = [
    'Sunrisers Hyderabad',
    'Mumbai Indians',
    'Royal Challengers Bangalore',
    'Kolkata Knight Riders',
    'Punjab Kings',
    'Chennai Super Kings',
    'Rajasthan Royals',
    'Delhi Capitals'
]

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah', 'Mohali', 'Bengaluru']

pipe = pickle.load(open('pickl.pkl','rb'))
st.title('IPL Win Predictor')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select the batting team',sorted(teams))

team2 = [team for team in teams if team != batting_team]

with col2:
    bowling_team = st.selectbox('Select the bowling team',sorted(team2))

selected_city = st.selectbox('Select host city',sorted(cities))

target = st.number_input("Target", min_value=1, max_value=350, step=1, format="%d")

col3,col4,col5 = st.columns(3)

with col3:
    score = st.number_input("Score", min_value=0, max_value=target, step=1, format="%d")
    if( score >= target):
        st.toast("Score should be less than target", icon="⚠️")
        st.stop()

with col4:
    overs = st.number_input("Overs completed", min_value=1, max_value=20, step=1, format="%d")


with col5:
    wickets = st.number_input("Wickets out", min_value=0, max_value=10, step=1, format="%d")

if st.button('Predict Probability'):
    runs_left = target - score
    balls_left = 120 - (overs*6)
    wickets = 10 - wickets
    crr = score/overs
    rrr = (runs_left*6)/balls_left

    input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[selected_city],'runs_left':[runs_left],'balls_left':[balls_left],'wickets':[wickets],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})

    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.header(batting_team + "- " + str(round(win*100)) + "%")
    st.header(bowling_team + "- " + str(round(loss*100)) + "%")

