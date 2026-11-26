
## Smart ATS

### Description

Smart ATS is a Streamlit-based web application that helps users improve their resumes by evaluating them against job descriptions using an OpenAI model (default `gpt-4o-mini`, configurable). The application supports both PDF and DOCX resume files and provides a detailed analysis, including job description match percentage, missing keywords, and a profile summary.

### Repository Structure

- **application_ats.py**: The main application file containing the Streamlit code.
- **.env.example**: Template for your `.env` file with the OpenAI API key (the real `.env` is git-ignored).
- **requirements.txt**: Python dependencies.
- **style.css**: A file containing custom CSS styles for the application.

### Files

1. **application_ats.py**

   This is the main application file. It sets up the Streamlit interface, handles file uploads, extracts text from PDF and DOCX files, sends the text to the OpenAI API for analysis, and displays the results.

2. **.env** (you create it from `.env.example`)

   This file contains your OpenAI API key and is git-ignored, so it is never committed. It should look something like this:

   ```
   OPENAI_API_KEY="your_openai_api_key_here"
   ```

3. **style.css**

   This file contains custom CSS styles to enhance the appearance of the application. An example of `style.css`:

   ```css
   body {
       background-color: #f0f2f6;
       color: #333;
   }

   h1 {
       color: skyblue;
   }

   .text {
       font-family: 'Arial';
       font-size: 16px;
   }
   ```

### How to Run

#### Prerequisites

- Python 3.9 or higher
- An OpenAI API key (usage is billed by OpenAI)

#### Steps to Run the Application

1. **Clone the Repository**

   ```sh
   git clone https://github.com/harshpatil01/Smart-ATS.git
   cd Smart-ATS
   pip install -r requirements.txt
   ```

2. **Set Up the Environment**

   Copy `.env.example` to `.env` and add your OpenAI API key.

   ```sh
   cp .env.example .env
   ```

3. **Run the Application**

   Use Streamlit to run the application.

   ```sh
   streamlit run application_ats.py
   ```

4. **Access the Application**

   Open your web browser and go to the URL provided by Streamlit.

### Usage

1. **Paste the Job Description**: Enter the job description in the text area provided.
2. **Upload Your Resume**: Upload your resume in PDF or DOCX format.
3. **Submit**: Click the "Submit" button to get the analysis.
4. **View Results**: The application will display the job description match percentage, missing keywords, and a profile summary.


### Limitations

- The match percentage is the language model's estimate, not a score from a real applicant tracking system. Treat it as a rough guide.
- Results can vary between runs for the same resume and job description.
- Resume text is sent to the OpenAI API, so don't upload documents you are not comfortable sharing with a third-party service.

## License

Code is released under the [MIT License](LICENSE). Datasets keep their original source licences.
