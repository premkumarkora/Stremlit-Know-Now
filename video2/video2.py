import streamlit as st

st.set_page_config(
    page_title="How to Create a Simple Webform Using Streamlit",
    page_icon="✅",
    layout="wide"
    )

st.markdown('<div style="text-align: center;"><h1>Kora Consultants</H1></div>', unsafe_allow_html=True)

name = st.text_input("Name")

age = st.selectbox( 'Age', (21,22,23,24,25,26,27,28,29))

location = st.radio( "Location", ('India', 'UK', 'USA', 'Canada', 'Australia'))

agree = st.checkbox('I agree the Terms and Conditions')

submit = st.button('Submit')

if submit:
    if agree:
        st.write('Thank You for the information, We will get back as soon as possible.')
        st.write('Your Name : ', name)
        st.write('Your Age :', age)
        st.write('Your Location  :', location)
    else:
        st.write('Accept Terms and Conditions before your proceed any further')
