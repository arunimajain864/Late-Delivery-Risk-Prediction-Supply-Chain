import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="APL Logistics Dashboard",
    layout="wide"
)

df = pd.read_csv("risk_predictions.csv")

st.title(
    "Late Delivery Risk Prediction Dashboard"
)

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Total Orders",
    len(df)
)

col2.metric(
    "High Risk Orders",
    len(
        df[
            df['Risk_Category']
            == 'High Risk'
        ]
    )
)

col3.metric(
    "Medium Risk Orders",
    len(
        df[
            df['Risk_Category']
            == 'Medium Risk'
        ]
    )
)

col4.metric(
    "Average Risk",
    round(
        df['Risk_Probability'].mean(),
        2
    )
)


st.subheader(
    "Risk Distribution"
)

fig = px.histogram(
    df,
    x='Risk_Probability'
)

st.plotly_chart(
    fig,
    use_container_width=True
)


st.subheader(
    "Region Risk Analysis"
)

region_risk = (

    df.groupby(
        'Order Region'
    )['Risk_Probability']
    .mean()
    .reset_index()
)

fig2 = px.bar(
    region_risk,
    x='Order Region',
    y='Risk_Probability'
)

st.plotly_chart(
    fig2,
    use_container_width=True
)



st.subheader(
    "Shipping Mode Risk"
)

mode_risk = (

    df.groupby(
        'Shipping Mode'
    )['Risk_Probability']
    .mean()
    .reset_index()
)

fig3 = px.bar(
    mode_risk,
    x='Shipping Mode',
    y='Risk_Probability'
)

st.plotly_chart(
    fig3,
    use_container_width=True
)


st.subheader(
    "High Risk Orders"
)

high_risk = df[
    df['Risk_Category']
    == 'High Risk'
]

st.dataframe(
    high_risk.head(100)
)
