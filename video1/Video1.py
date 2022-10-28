import streamlit as st
import plotly.express as px

st.write("Welcome")

st.markdown('<div style="text-align: center;"><h1>Kora Consultants</H1></div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center;"><p>Let us leran Stremlit from basics </p>', unsafe_allow_html=True)

line_chart = px.line(
    x=[1,3,5,7,9],
    y=[2,4,8,12,16],
    width=400,
    height=350
)
st.plotly_chart(line_chart)
