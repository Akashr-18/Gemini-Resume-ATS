import os
import streamlit as st
import PyPDF2 as pdf
from PIL import Image
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
MODEL_NAME = "gemini-1.5-flash-002"

def get_gemini_response(input):
    generation_config = {"temperature": 0, "max_output_tokens": 10000} 
    model = genai.GenerativeModel(MODEL_NAME , generation_config = generation_config)
    response = model.generate_content(input)
    return response.text

def get_pdf_content(uploaded_file):
    pdf_content = ""
    reader = pdf.PdfReader(uploaded_file)
    for page in range(len(reader.pages)):
        page_text = reader.pages[page]
        pdf_content += str(page_text.extract_text())
    return pdf_content

input_prompt=f"""
You are an experienced ATS(Application Tracking System) with a deep understanding of artificial intelligence,data science ,data analyst and big data engineering. 
You will be provided with 'resume' and 'job_decription'.Your task is to evaluate the 'resume' based on the given 'job_decription'.
Given how competitive the job market is, you should offer your finest help in order to help the 'resume' stand out. \
Assign the percentage Matching based on 'job_decription' and the missing keywords with high accuracy.\
resume:{pdf_content}
job_decription:{jd}
Provide your output in dictionary format with the following Keys "JD Match percentage", "MissingKeywords" and "Suggestion"
"""

custom_css = """
<style>
    body { background-color: #ffffff !important; }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)
st.title("Smart ATS: Optimize Your Resume")
jd=st.text_area("Job Description")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please uplaod your Resume in pdf format")
submit = st.button("Analyze Resume")

if submit:
    
    if uploaded_file is not None:
        pdf_content = get_pdf_content(uploaded_file)
        response = get_gemini_response(input_prompt)
        st.subheader("Response: ")
        st.write(response)
    else:
        pass
        
else:
    pass
