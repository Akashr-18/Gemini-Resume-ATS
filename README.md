# Streamlit Application: Smart ATS

This Streamlit application is designed to help evaluate resumes based on a provided job description using Gemini model by Google.

## Features

- Upload your resume in PDF format.
- Enter a job description to evaluate the resume against.
- Get analysis results including job description match percentage, missing keywords and insightful recommendations.

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

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

2. Open your web browser and go to [http://localhost:8501](http://localhost:8501).

3. Upload your resume and enter the job description to analyze the resume.

Here's the screenshot of the Streamlit application:
![Streamlit Application Screenshot](https://imgur.com/a/qys2z2e)

Home page :

<img width="960" alt="image" src="https://github.com/Akashr-18/Data_Store/blob/main/Screenshot%20(2).png?raw=true">

After prediction:

<img width="959" alt="image" src="https://user-images.githubusercontent.com/58848985/169639225-12196595-7de7-47bf-bcde-73610e5b28b0.png">

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
