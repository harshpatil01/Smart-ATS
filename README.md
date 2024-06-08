
## Smart ATS

### Description

Smart ATS is a Streamlit-based web application that helps users improve their resumes by evaluating them against job descriptions using OpenAI's GPT-4. The application supports both PDF and DOCX resume files and provides a detailed analysis, including job description match percentage, missing keywords, and a profile summary.

### Repository Structure

- **application_ats.py**: The main application file containing the Streamlit code.
- **.env**: A file containing your OpenAI API key.
- **style.css**: A file containing custom CSS styles for the application.

### Files

1. **application_ats.py**

   This is the main application file. It sets up the Streamlit interface, handles file uploads, extracts text from PDF and DOCX files, sends the text to GPT-4 for analysis, and displays the results.

2. **.env**

   This file contains your OpenAI API key. It should look something like this:

   ```
   OPENAI_API_KEY=your_openai_api_key_here
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

1. **Python 3.7 or higher**: Ensure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/).

2. **Streamlit**: Install Streamlit if you haven't already.

   ```sh
   pip install streamlit
   ```

3. **OpenAI**: Install the OpenAI package.

   ```sh
   pip install openai
   ```

4. **PyPDF2**: Install PyPDF2 for PDF text extraction.

   ```sh
   pip install PyPDF2
   ```

5. **python-docx**: Install python-docx for DOCX text extraction.

   ```sh
   pip install python-docx
   ```

6. **python-dotenv**: Install python-dotenv to manage environment variables.

   ```sh
   pip install python-dotenv
   ```

#### Steps to Run the Application

1. **Clone the Repository**

   ```sh
   git clone https://github.com/yourusername/smart-ats.git
   cd smart-ats
   ```

2. **Set Up the Environment**

   Create a `.env` file in the root directory of the project and add your OpenAI API key.

   ```
   OPENAI_API_KEY=your_openai_api_key_here
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

