import pickle
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Churn Prediction", page_icon="img/mba_usp_esalq.jpg")
st.sidebar.header('File Prediction')
st.title("Batch churn prediction")

st.markdown("Predict churn using a csv file:")

# -- Model -- #
with open('models/cluster_pipeline.pkl', 'rb') as file:
    cluster_pipeline = pickle.load(file)

with open('models/prediction_pipeline.pkl', 'rb') as file:
    prediction_pipeline = pickle.load(file)

data = st.file_uploader('Upload your file')
if data:
    df_input = pd.read_csv(data)
    # Predict cluster
    try:
        df_input['cluster'] = cluster_pipeline.predict(df_input)
    except:
        df_input['cluster'] = -1
    # Predict churn
    prediction_probability = prediction_pipeline.predict_proba(df_input)[:,1]
    churn_prediction = prediction_pipeline.predict(df_input)
    df_output = (
        df_input
        .assign(
            prediction_probability = prediction_probability,
            churn_prediction = churn_prediction
            )
        )

    st.markdown('Churn prediction:')
    st.write(df_output)
    st.download_button(
        label='Download CSV', data=df_output.to_csv(index=False).encode('utf-8'),
        mime='text/csv', file_name='predicted_churn.csv'
        )

