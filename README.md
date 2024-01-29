# Streamlit Application: Smart ATS

This Streamlit application is designed to help evaluate resumes based on a provided job description using Gemini model by Google.

## Features

- Upload your resume in PDF format.
- Enter a job description to evaluate the resume against.
- Get analysis results including job description match percentage, missing keywords and insightful recommendations.

## Built With

 - Google-generativeai
 - Streamlit
 - PyPDF2

## Models used

 - gemini-pro
   
## Getting Started

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Akashr-18/Gemini-Resume-ATS.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Gemini-Resume-ATS
    ```

3. Create a Virtual Environment (Optional but recommended)

     ```bash
     conda create -p <Environment_Name> python==<python version> -y
     ```

4. Activate the Virtual Environment (Optional)

      ```
      conda activate <Environment_Name>/
      ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Make sure you create a file named .env and store your Google API key

### Usage

1. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

2. Open your web browser and go to [http://localhost:8501](http://localhost:8501).

3. Upload your resume and enter the job description to analyze the resume.

#### Home page :

<img width="960" alt="image" src="https://github.com/Akashr-18/Data_Store/blob/main/Screenshot%20(9).png?raw=true">
<br>

#### Copy the job description :

<img width="960" alt="image" src="https://github.com/Akashr-18/Data_Store/blob/main/Screenshot%20(5).png?raw=true">
<br>

#### Paste the job description :

<img width="960" alt="image" src="https://github.com/Akashr-18/Data_Store/blob/main/Screenshot%20(7).png?raw=true">
<br>

#### Output After Resume Analysis:

<img width="959" alt="image" src="https://github.com/Akashr-18/Data_Store/blob/main/Screenshot%20(8).png?raw=true">
<br>

## Contributing

Contributions are welcome! Here's how you can contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/new-feature`.
3. Make your changes and commit them: `git commit -am 'Add new feature'`.
4. Push to the branch: `git push origin feature/new-feature`.
5. Submit a pull request.

Please make sure to update tests as appropriate.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
