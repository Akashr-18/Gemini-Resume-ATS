import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
import PyPDF2 as pdf
from pathlib import Path

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

def get_pdf_content(uploaded_file):
    pdf_content = ""
    reader = pdf.PdfReader(uploaded_file)
    for page in range(len(reader.pages)):
        page_text = reader.pages[page]
        pdf_content += str(page_text.extract_text())
    return pdf_content

input_prompt="""
You are an experienced ATS(Application Tracking System) with a deep understanding of artificial intelligence,data science ,data analyst and big data engineering. 
You will be provided with 'resume' and 'job_decription'.Your task is to evaluate the 'resume' based on the given 'job_decription'.
Given how competitive the job market is, you should offer your finest help in order to help the 'resume' stand out. 
Assign the percentage Matching based on 'job_decription' and the missing keywords with high accuracy
resume:{pdf_content}
job_decription:{jd}

Provide the output as json with "JD Match percentage", "MissingKeywords", "Suggestion" as keys
Output type:
"JD Match percentage" : Number, 
"MissingKeywords" : List,
"Suggestion" : String
"""
# I want the response in one single string having the structure
# {{"JD Match percentage":"%","MissingKeywords:[]","Profile Summary":""}}

def set_background(color):
    if color:
        hex_color = f"#{color}"
        st.markdown(
            f"""
            <style>
            body {{
                background-color: {hex_color};
            }}
            </style>
            """,
            unsafe_allow_html=True,
        )

background_color = "FFFFFF"  # Hex code for white
set_background(background_color)
# Add CSS for background image

# def set_background(style):
#     if style:
#         st.markdown(
#             f"""
#             <style>
#             .reportview-container {{
#                 background: url("{style}") no-repeat center center fixed;
#                 background-size: cover;
#             }}
#             </style>
#             """,
#             unsafe_allow_html=True,
#         )

# background_image = r"C:\Users\Akash R\OneDrive\Pictures\Background\pexels-miguel-á-padriñán-255379.jpg"
# background_image = Path(r"C:\Users\Akash R\OneDrive\Pictures\Background\pngtree-modern-double-color-futuristic-neon-background-image_351866.jpg")
# set_background(background_image)

st.title("Smart ATS: Optimize Your Resume")

jd=st.text_area("Job Description")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please uplaod your Resume in pdf format")

submit = st.button("Analyze Resume")

if submit:
    if uploaded_file is not None:
        pdf_content = get_pdf_content(uploaded_file)
        response = get_gemini_response(input_prompt)
        st.subheader("Response: ")
        # response = eval(response)
        # st.subheader("JD Match Percentage")
        # st.write(response['JD Match percentage'])
        # st.subheader("Missing Keywords")
        # st.write(response['MissingKeywords'])
        # st.subheader("Suggestion")
        # st.write(response['Suggestion'])

        st.write(response)
    else:
        pass
else:
    pass
