# ====================== IMPORT PACKAGES ==============

import pandas as pd
import time
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import linear_model
from sklearn import metrics
import matplotlib.pyplot as plt
import os
import numpy as np
import warnings
warnings.filterwarnings("ignore")
from sklearn import preprocessing 

import streamlit as st
import base64
import streamlit as st
from faker import Faker
import pickle
from fpdf import FPDF
from streamlit_option_menu import option_menu


 # ------------ TITLE 

st.markdown(f'<h1 style="color:#8d1b92;text-align: center;font-size:36px;">{"Shadow Net"}</h1>', unsafe_allow_html=True)


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



  
selected = option_menu(
    menu_title=None, 
    options=["Prediction","Dashboard","Graph","Report"],  
    orientation="horizontal",
)


st.markdown(
    """
    <style>
    .option_menu_container {
        position: fixed;
        top: 20px;
        right: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


if selected=="Prediction":

    
    import pickle
    
    with open('model.pickle', 'rb') as f:
        rf = pickle.load(f)
        
        
        
        
    with open('finalpred.pickle', 'rb') as f:
         pred_rf = pickle.load(f)  
         
    
    
    # pred_rf = pred_rf
    
    # ================== PREDICTION  ====================
    
    st.write("-----------------------------------")
    st.write("          Prediction               ")
    st.write("-----------------------------------")
    
    
    inpp = st.text_input("Enter Prediction Index Number = ")
    
    butt = st.button("Submit")
    
    if butt:
    
            
        if pred_rf[int(inpp)] == 0:
            st.markdown(f'<h1 style="color:#0000FF;text-align: center;font-size:28px;font-family:Caveat, sans-serif;">{"Identified = BRUTE FORCE"}</h1>', unsafe_allow_html=True)
            
            aa="Identified = BRUTE FORCE"
    
            from faker import Faker
            ex = Faker()
            ip_rec = ex.ipv4()
            ip_sen = ex.ipv4()
            
            
            st.write("Sender's IP Address   = ",ip_sen )
            st.write("Reciever's IP Address = ",ip_rec )
            
            
            import pickle
            with open('Cloud/file.pickle', 'wb') as f:
                pickle.dump(aa, f)
                
                
    # Create a PDF to save the results
            pdf = FPDF()
            pdf.add_page()
        
            # Set font for the PDF
            pdf.set_font('Arial', 'B', 16)
        
            # Add Title
            pdf.cell(200, 10, txt="Brute Force Identification Report", ln=True, align='C')
        
            # Set font for the content
            pdf.set_font('Arial', '', 12)
        
            # Add the content
            pdf.ln(10)
            pdf.cell(200, 10, txt="Identification Result: " + aa, ln=True)
            pdf.cell(200, 10, txt="Sender's IP Address: " + ip_sen, ln=True)
            pdf.cell(200, 10, txt="Receiver's IP Address: " + ip_rec, ln=True)
        
            # Save the PDF to file
            pdf_output = "Cloud/Report.pdf"
            pdf.output(pdf_output)
        
                
                
        elif pred_rf[int(inpp)] == 1:
            st.markdown(f'<h1 style="color:#0000FF;text-align: center;font-size:28px;font-family:Caveat, sans-serif;">{"Identified = HTTP DDoS"}</h1>', unsafe_allow_html=True)
    
    
    
            aa="Identified = HTTP DDoS"
    
            from faker import Faker
            ex = Faker()
            ip_rec = ex.ipv4()
            ip_sen = ex.ipv4()
            
            
            st.write("Sender's IP Address   = ",ip_sen )
            st.write("Reciever's IP Address = ",ip_rec )
            
            import pickle
            with open('Cloud/file.pickle', 'wb') as f:
                pickle.dump(aa, f)
    
                
    # Create a PDF to save the results
            pdf = FPDF()
            pdf.add_page()
        
            # Set font for the PDF
            pdf.set_font('Arial', 'B', 16)
        
            # Add Title
            pdf.cell(200, 10, txt="HTTP DDOS Identification Report", ln=True, align='C')
        
            # Set font for the content
            pdf.set_font('Arial', '', 12)
        
            # Add the content
            pdf.ln(10)
            pdf.cell(200, 10, txt="Identification Result: " + aa, ln=True)
            pdf.cell(200, 10, txt="Sender's IP Address: " + ip_sen, ln=True)
            pdf.cell(200, 10, txt="Receiver's IP Address: " + ip_rec, ln=True)
        
            # Save the PDF to file
            pdf_output = "Cloud/Report.pdf"
            pdf.output(pdf_output)
        
            # st.write(f"PDF report saved at: {pdf_output}")    
    
        elif pred_rf[int(inpp)] == 2:
            st.markdown(f'<h1 style="color:#0000FF;text-align: center;font-size:28px;font-family:Caveat, sans-serif;">{"Identified = INSIDER THREAT"}</h1>', unsafe_allow_html=True)
    
    
            aa="Identified = INSIDER THREAT"
    
            from faker import Faker
            ex = Faker()
            ip_rec = ex.ipv4()
            ip_sen = ex.ipv4()
            
            
            st.write("Sender's IP Address   = ",ip_sen )
            st.write("Reciever's IP Address = ",ip_rec )     
            
            import pickle
            with open('Cloud/file.pickle', 'wb') as f:
                pickle.dump(aa, f)
    
                
    # Create a PDF to save the results
            pdf = FPDF()
            pdf.add_page()
        
            # Set font for the PDF
            pdf.set_font('Arial', 'B', 16)
        
            # Add Title
            pdf.cell(200, 10, txt="INSIDER THREAT Identification Report", ln=True, align='C')
        
            # Set font for the content
            pdf.set_font('Arial', '', 12)
        
            # Add the content
            pdf.ln(10)
            pdf.cell(200, 10, txt="Identification Result: " + aa, ln=True)
            pdf.cell(200, 10, txt="Sender's IP Address: " + ip_sen, ln=True)
            pdf.cell(200, 10, txt="Receiver's IP Address: " + ip_rec, ln=True)
        
            # Save the PDF to file
            pdf_output = "Cloud/Report.pdf"
            pdf.output(pdf_output)
        
            st.write(f"PDF report saved at: {pdf_output}")    
    
        elif pred_rf[int(inpp)] == 3:
            st.markdown(f'<h1 style="color:#0000FF;text-align: center;font-size:28px;font-family:Caveat, sans-serif;">{"Identified = MAN IN THE MIDDLE ATTACK"}</h1>', unsafe_allow_html=True)
    
            
            aa="Identified = MAN IN THE MIDDLE ATTACK"
            from faker import Faker
            ex = Faker()
            ip_rec = ex.ipv4()
            ip_sen = ex.ipv4()
            
            
            st.write("Sender's IP Address   = ",ip_sen )
            st.write("Reciever's IP Address = ",ip_rec )   
            
            import pickle
            with open('Cloud/file.pickle', 'wb') as f:
                pickle.dump(aa, f)
                
            pdf = FPDF()
            pdf.add_page()
        
            # Set font for the PDF
            pdf.set_font('Arial', 'B', 16)
        
            # Add Title
            pdf.cell(200, 10, txt="MAN IN THE MIDDLE ATTACK Identification Report", ln=True, align='C')
        
            # Set font for the content
            pdf.set_font('Arial', '', 12)
        
            # Add the content
            pdf.ln(10)
            pdf.cell(200, 10, txt="Identification Result: " + aa, ln=True)
            pdf.cell(200, 10, txt="Sender's IP Address: " + ip_sen, ln=True)
            pdf.cell(200, 10, txt="Receiver's IP Address: " + ip_rec, ln=True)
        
            # Save the PDF to file
            pdf_output = "Cloud/Report.pdf"
            pdf.output(pdf_output)
                    
                
                
                
                
                
            
        elif pred_rf[int(inpp)] == 4:
            st.markdown(f'<h1 style="color:#0000FF;text-align: center;font-size:28px;font-family:Caveat, sans-serif;">{"Identified = NORMAL "}</h1>', unsafe_allow_html=True)
    
    
            aa="Identified = NORMAL"
    
            import pickle
            with open('Cloud/file.pickle', 'wb') as f:
                pickle.dump(aa, f)
    
    
            # pdf = FPDF()
            # pdf.add_page()
        
            # # Set font for the PDF
            # pdf.set_font('Arial', 'B', 16)
        
            # # Add Title
            # pdf.cell(200, 10, txt="NORMAL ATTACK Identification Report", ln=True, align='C')
        
            # # Set font for the content
            # pdf.set_font('Arial', '', 12)
        
            # # Add the content
            # pdf.ln(10)
            # pdf.cell(200, 10, txt="Identification Result: " + aa, ln=True)
            # pdf.cell(200, 10, txt="Sender's IP Address: " + ip_sen, ln=True)
            # pdf.cell(200, 10, txt="Receiver's IP Address: " + ip_rec, ln=True)
        
            # # Save the PDF to file
            # pdf_output = "Cloud/Report.pdf"
            # pdf.output(pdf_output)
        
    
    
    
        elif pred_rf[int(inpp)] == 5:
            st.markdown(f'<h1 style="color:#0000FF;text-align: center;font-size:28px;font-family:Caveat, sans-serif;">{"Identified = PORT SCANNING "}</h1>', unsafe_allow_html=True)
    
            
            aa="Identified = PORT SCANNING"
    
            from faker import Faker
            ex = Faker()
            ip_rec = ex.ipv4()
            ip_sen = ex.ipv4()
            
            
            st.write("Sender's IP Address   = ",ip_sen )
            st.write("Reciever's IP Address = ",ip_rec )  
            
            import pickle
            with open('Cloud/file.pickle', 'wb') as f:
                pickle.dump(aa, f)
        
            pdf = FPDF()
            pdf.add_page()
        
            # Set font for the PDF
            pdf.set_font('Arial', 'B', 16)
        
            # Add Title
            pdf.cell(200, 10, txt="PORT SCANNING Identification Report", ln=True, align='C')
        
            # Set font for the content
            pdf.set_font('Arial', '', 12)
        
            # Add the content
            pdf.ln(10)
            pdf.cell(200, 10, txt="Identification Result: " + aa, ln=True)
            pdf.cell(200, 10, txt="Sender's IP Address: " + ip_sen, ln=True)
            pdf.cell(200, 10, txt="Receiver's IP Address: " + ip_rec, ln=True)
        
            # Save the PDF to file
            pdf_output = "Cloud/Report.pdf"
            pdf.output(pdf_output)
        
if selected=="Dashboard":
    
    import os
    # Read the HTML file
    html_file_path = "templates/dash.html"
    
    # Make sure the HTML file exists
    if os.path.exists(html_file_path):
        with open(html_file_path, 'r') as file:
            html_content = file.read()
    
        # Display the HTML content
        st.components.v1.html(html_content, height=600)
    else:
        st.error("HTML file not found.")
    
    
    
            
if selected=="Graph":
    
    st.image("network_traffic_zigzag.gif")
    
    
if selected=="Report":
    
    
    pdf_output = "Cloud/Report.pdf"
    # Provide the download button for the user
    with open(pdf_output, "rb") as pdf_file:
        st.download_button(
            label="Download PDF Report",
            data=pdf_file,
            file_name="Report.pdf",
            mime="application/pdf"
        )  
    
    
    
    
    
    