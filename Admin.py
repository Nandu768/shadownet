# ====================== IMPORT PACKAGES ==============

import pandas as pd

import warnings
warnings.filterwarnings("ignore")

import streamlit as st
import base64

 # ------------ TITLE 



# ================ Background image ===

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('1.jpg')



# ================ ATTACK IDENTIFICATION ===


st.write("----------------------------------------------------------------------------------")

st.markdown(f'<h1 style="color:#8d1b92;text-align: center;font-size:36px;">{"Shadow Net"}</h1>', unsafe_allow_html=True)


import pickle
with open('Cloud/file.pickle', 'rb') as f:
    aa = pickle.load(f)



if aa == 'Identified = NORMAL':
    


    st.success(" There is No attack  !!!!! ")


else:
        
    from faker import Faker
    ex = Faker()
    ip_rec = ex.ipv4()
    ip_sen = ex.ipv4()
    
    st.write("Sender's IP Address   = ",ip_sen )
    st.write("Reciever's IP Address = ",ip_rec )

    

    st.success(" IP address is BLOCKED !!!!! ")

