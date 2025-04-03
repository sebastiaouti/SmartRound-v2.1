
import streamlit as st
from SmartCheck import smartcheck_interface
from SmartRound import smartround_interface
from SmartRound_UTI import smartround_uti_interface

st.set_page_config(page_title="SmartRound", layout="wide")

st.markdown("<h1 style='text-align: center;'>SmartRound</h1>", unsafe_allow_html=True)

st.sidebar.title("SmartRound")
st.sidebar.write("Escolha uma função:")
opcao = st.sidebar.radio("", ["SmartCheck", "SmartRound Enfermaria", "SmartRound UTI"])
st.sidebar.markdown("---")
st.sidebar.markdown("<div style='position: absolute; bottom: 20px;'>By Sebastião Almeida</div>", unsafe_allow_html=True)

if opcao == "SmartCheck":
    smartcheck_interface()
elif opcao == "SmartRound Enfermaria":
    smartround_interface()
elif opcao == "SmartRound UTI":
    smartround_uti_interface()
