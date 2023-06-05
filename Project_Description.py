import streamlit as st

st.set_page_config(
    page_title="Churn Prediction 📡",
    page_icon="img/mba_usp_esalq.jpg",
)

st.sidebar.header('Project Description')

st.write("# 📡 Churn Prediction App 📡")
st.write("\n\n")

st.markdown("""
**Author:** Cainã Max Couto da Silva  
**LinkedIn:** [@cmcouto-silva](https://www.linkedin.com/in/cmcouto-silva/)
""")
            
st.image('img/churn-icon.png')
st.write("\n\n")

st.markdown(
    """
    We build an hybrid ML approach to cluster customers and predict churn using the [IBM Telco Dataset](https://community.ibm.com/community/user/businessanalytics/blogs/steven-macko/2019/07/11/telco-customer-churn-1113).
    Please refer to [this repo](https://github.com/cmcouto-silva/telco-churn) for details.

    This App predicts churn based in the following input features:
    - CLTV
    - Contract
    - Dependents
    - Device Protection
    - Internet Service
    - Monthly Charges
    - Multiple Lines
    - Online Backup
    - Online Security
    - Paperless Billing
    - Partner
    - Payment Method
    - Senior Citizen
    - Streaming Movies
    - Streaming TV
    - Tech Support
    - Tenure Months
    - Total Charges
    """
)

st.success('Please **go to the next pages** to get the predictions.')
