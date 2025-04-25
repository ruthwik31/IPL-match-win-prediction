# IPL Win Predictor

This project is an interactive web app that predicts the winning probabilities of Indian Premier League (IPL) cricket teams during a match, built using Streamlit and a trained machine learning model.

# Project Overview

<h4>Objective:</h4>
Predict the outcome (winning team) of IPL matches using historical match and delivery data.<br>
<h4>Approach:</h4>
The notebook processes and merges match-level and ball-by-ball datasets, engineers relevant features, and trains a Random Forest classifier to predict match outcomes based on the current match situation.

## Features

<ul>
  <li>Batting team</li>
  <li>Bowling team</li>
  <li>City</li>
</ul>

<h3>Numerical:</h3>
<ul>
  <li>Runs left</li>
  <li>Balls left</li>
  <li>Wickets remaining</li>
  <li>Total runs to chase</li>
  <li>Current run rate (CRR)</li>
  <li>Required run rate (RRR)</li>
</ul>

## Pipeline & Model

- Preprocessing:
Categorical features are encoded using OneHotEncoder.
Numerical features are scaled with StandardScaler.<br>
- Model:
<p><strong>RandomForestClassifier</strong>is used for prediction. It uses a trained Random Forest classifier (from scikit-learn).<br>
Inputs: <strong>Batting team</strong>, <strong>Bowling team</strong>, <strong>City</strong>, <strong>Runs left</strong>, <strong>Balls left</strong>, <strong>Wickets in hand</strong>, <strong>Target</strong>, <strong>Current run rate (CRR)</strong>, and <strong>Required run rate (RRR)</strong>.<br>
Outputs: <strong>win probabilities</strong> for both teams.
</p>
<br>
- Pipeline:
All preprocessing and modeling steps are combined into a scikit-learn Pipeline for streamlined training and inference.

## models used
- logistic regression
- Random Forest
- xgboost
And i have evaluated on RandomForestClassifier ,then stored the trained data into .pkl file.
## How it works

- Select Teams & City: Choose batting and bowling teams, and the host city.
- Set Match Situation: Enter the target score, current score, overs completed, and wickets fallen.
- Predict: Click "Predict Probability" to view each team's win percentage.

## to run GuiApp.py
streamlit run GuiApp.py