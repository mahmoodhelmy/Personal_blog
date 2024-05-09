import  streamlit as st
import smtplib ,ssl
st.set_page_config(
    page_title="Nerdy Beardy Blog",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={'About':"# MY personal Blog"}

)
st.title("The Nerdy Beardy Blog")

mail = st.text_input("Your email here")
choi=st.multiselect("Choose mail topic",['Chat','Help','Support','other'])
messe = st.text_area("Your message")

