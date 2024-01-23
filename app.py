import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
import PyPDF2 as pdf

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def get_gemini_response(input, pdf_content, prompt):
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
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Jd and
the missing keywords with high accuracy
resume:{pdf_content}
description:{jd}

I want the response in one single string having the structure
{{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
"""

#StreamLit App
st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd=st.text_area("Paste the Job Description")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please uplaod your Resume in pdf format")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        pdf_content = get_pdf_content(uploaded_file)
        response = get_gemini_response(input_prompt)
        st.subheader("Response: ")
        st.write(response)