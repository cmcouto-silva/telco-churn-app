import pickle
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Churn Prediction", page_icon="img/mba_usp_esalq.jpg")
st.sidebar.header('What if Prediction')
st.title("Churn prediction")

st.markdown("Predict medical insurance based on the following features:")

# -- Parameters -- #

cltv = st.number_input(label='CLTV', value=4400, min_value=0)
contract = st.selectbox(label='Contract', options=['Month-to-month', 'One year', 'Two year'])
dependents = st.selectbox(label='Dependents', options=['No','Yes'])
device_protection = st.selectbox(label='Device Protection', options=['No', 'No internet service', 'Yes'])
internet_service = st.selectbox(label='Internet Service', options=['DSL', 'Fiber optic', 'No'])
monthly_charges = st.number_input(label='Monthly Charges', value=65, min_value=0)
multiple_lines = st.selectbox(label='Multiple Lines', options=['No', 'No phone service', 'Yes'])
online_backup = st.selectbox(label='Online Backup', options=['No', 'No internet service', 'Yes'])
online_security = st.selectbox(label='Online Security', options=['No', 'No internet service', 'Yes'])
paperless_billing = st.selectbox(label='Paperless Billing', options=['No','Yes'])
partner = st.selectbox(label='Partner', options=['No','Yes'])
payment_method = st.selectbox(label='Payment Method', options=['Bank transfer (automatic)', 'Credit card (automatic)', 'Electronic check', 'Mailed check'])
senior_citizen = st.selectbox(label='Senior Citizen', options=['No','Yes'])
streaming_movies = st.selectbox(label='Streaming Movies', options=['No', 'No internet service', 'Yes'])
streaming_tv = st.selectbox(label='Streaming TV', options=['No', 'No internet service', 'Yes'])
tech_support = st.selectbox(label='Tech Support', options=['No', 'No internet service', 'Yes'])
tenure_months = st.number_input(label='Tenure Months', value=32, min_value=0)
total_charges = st.number_input(label='Total Charges', value=2283, min_value=0)

# -- Model -- #

with open('models/cluster_pipeline.pkl', 'rb') as file:
    cluster_pipeline = pickle.load(file)

with open('models/prediction_pipeline.pkl', 'rb') as file:
    prediction_pipeline = pickle.load(file)

def prediction():
    df_input = pd.DataFrame([{
        'CLTV': cltv,
        'Contract': contract,
        'Dependents':dependents,
        'Device Protection':device_protection,
        'Internet Service': internet_service,
        'Monthly Charges': monthly_charges,
        'Multiple Lines': multiple_lines,
        'Online Backup': online_backup,
        'Online Security': online_security,
        'Paperless Billing': paperless_billing,
        'Partner': partner,
        'Payment Method': payment_method,
        'Senior Citizen': senior_citizen,
        'Streaming Movies': streaming_movies,
        'Streaming TV': streaming_tv,
        'Tech Support': tech_support,
        'Tenure Months': tenure_months,
        'Total Charges': total_charges
        }])
    try:
        df_input['cluster'] = cluster_pipeline.predict(df_input)
    except:
        df_input['cluster'] = -1
    prediction_proba = prediction_pipeline.predict_proba(df_input)[0,1]
    return prediction_proba

# Predict
if st.button('Predict'):
    try:
        churn_output = prediction()
        st.success(f'**Predicted churn:** {churn_output:.2f} ({churn_output>0.5})')
    except Exception as error:
        st.error(f"Couldn't predict the input data. The following error occurred: \n\n{error}")

