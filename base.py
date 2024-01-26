import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
import PyPDF2 as pdf

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Google API
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Function to get response from Gemini model
def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

# Function to extract text content from uploaded PDF file
def get_pdf_content(uploaded_file):
    pdf_content = ""
    reader = pdf.PdfReader(uploaded_file)
    for page in range(len(reader.pages)):
        page_text = reader.pages[page]
        pdf_content += str(page_text.extract_text())
    return pdf_content

# Main function for Streamlit app
def main():
    st.set_page_config(layout="wide")
    st.title("Smart ATS: Optimize Your Resume")

    # Sidebar with job description input
    st.sidebar.title("Job Description")
    jd = st.sidebar.text_area("Enter Job Description")

    # Main content area
    st.subheader("Upload Your Resume")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf", help="Upload your resume in PDF format")

    if uploaded_file is not None:
        # Display uploaded resume
        st.subheader("Uploaded Resume")
        st.write(uploaded_file.name)

        # Button to analyze resume
        if st.button("Analyze Resume"):
            pdf_content = get_pdf_content(uploaded_file)
            input_prompt = f"""
            You are an experienced ATS (Application Tracking System) with a deep understanding of artificial intelligence, data science, data analysis, and big data engineering. 
            You will be provided with a resume and job description. Your task is to evaluate the resume based on the given job description.
            Given how competitive the job market is, you should offer your finest help in order to help the resume stand out.
            Assign the percentage Matching based on the job description and the missing keywords with high accuracy.
            resume:{pdf_content}
            job_description:{jd}
            Provide the output as JSON with "JD Match percentage", "MissingKeywords", "Suggestion" as keys.
            """
            response = get_gemini_response(input_prompt)

            # Display analysis results
            st.subheader("Analysis Results")
            st.json(response)

# Run the app
if __name__ == "__main__":
    main()
