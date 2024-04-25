import streamlit as st
import joblib
import numpy as np
import wget

model_name = 'model.joblib'
file_url = 'https://github.com/Donein/German_car_insights/blob/main/model.joblib'
wget.download(file_url)
model = joblib.load(model_name)

def predictions(CreditScore,Geography,Gender,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary,Complain,Satisfaction_Score,Card_Type,Point_Earned):
    if Geography == 'France':
        Geography = 0
    elif Geography == 'Germany':
        Geography = 1
    else:
        Geography = 2

    if Gender == 'Female':
        Gender = 0
    else:
        Gender = 1

    if Card_Type == 'DIAMOND':
        Card_Type = 0
    elif Card_Type == 'GOLD':
        Card_Type = 1
    elif Card_Type == 'PLATINUM':
        Card_Type = 2
    else:
        Card_Type = 3

    prediction = model.predict([[CreditScore,Geography,Gender,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary,Complain,Satisfaction_Score,Card_Type,Point_Earned]])
    print(print(prediction))

    if prediction == 0:
        pred = 'Retained'
    else:
        pred = 'Exit'

    return pred

def main():
    st.title('Churn prediction of customers')
    st.header('Please enter the following details to know about the probable status of the customer')
    CreditScore = st.number_input('Credit Score')
    Geography = st.selectbox('Geography',('France','Germany','Spain'))
    Gender = st.selectbox('Gender',('Female','Male'))
    Age = st.number_input('Age')
    Tenure = st.selectbox('Tenure',(0,1,2,3,4,5,6,7,8,9,10))
    Balance = st.number_input('Balance')
    NumOfProducts = st.selectbox('NumOfProducts',(1,2,3,4))
    HasCrCard = st.selectbox('HasCrCard',(0,1))
    IsActiveMember = st.selectbox('IsActiveMember',(0,1))
    EstimatedSalary = st.number_input('EstimatedSalary')
    Complain = st.selectbox('Complain',(0,1))
    Satisfaction_Score = st.selectbox('Satisfaction Score',(1,2,3,4,5))
    Card_Type = st.selectbox('Card Type',('DIAMOND','GOLD','SILVER','PLATINUM'))
    Point_Earned = st.number_input('Point Earned')

    if st.button('Predict'):
        result = predictions(CreditScore,Geography,Gender,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary,Complain,Satisfaction_Score,Card_Type,Point_Earned)

        if result == 'Retained':
            st.success('Customer will remain')
        else:
            st.error('Customer will leave')

if __name__ == "__main__":
    main()



