import streamlit as st  # Import Streamlit for web interface
from openai import OpenAI  # OpenAI Python SDK (v1+)
import os  # Import os for environment variable access
import PyPDF2 as pdf  # Import PyPDF2 for PDF text extraction
import docx  # Import python-docx for DOCX text extraction
from dotenv import load_dotenv  # Import load_dotenv to load environment variables from .env file
import json  # Import json for handling JSON data

# Load environment variables from a .env file
load_dotenv()

# Create the OpenAI client. It reads the key from the OPENAI_API_KEY environment variable.
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Model used for the analysis. Override it with the OPENAI_MODEL environment variable if you like.
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

# Styling
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)  # Load and apply local CSS file

# This file should contain your CSS
local_css("style.css")

def get_gpt_response(input_text):
    """
    Sends the prompt to the OpenAI model and returns its reply.

    Parameters:
        input_text (str): The input prompt to send to the GPT-4 model.

    Returns:
        str: The text response from the model.
    """
    response = client.chat.completions.create(
        model=MODEL,
        response_format={"type": "json_object"},  # Ask for valid JSON so json.loads() below works
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},  # System message to set the assistant's behavior
            {"role": "user", "content": input_text}  # User message containing the input text
        ],
        max_tokens=500,  # Adjust based on the expected length of response
        temperature=0.7  # Adjust creativity level
    )
    return response.choices[0].message.content.strip()  # Return the generated response

def input_pdf_text(uploaded_file):
    """
    Extracts text from a PDF file.

    Parameters:
        uploaded_file (UploadedFile): The uploaded PDF file.

    Returns:
        str: The extracted text from the PDF.
    """
    reader = pdf.PdfReader(uploaded_file)  # Create a PDF reader object
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]  # Get each page
        text += str(page.extract_text())  # Extract text from each page
    return text

def input_docx_text(uploaded_file):
    """
    Extracts text from a DOCX file.

    Parameters:
        uploaded_file (UploadedFile): The uploaded DOCX file.

    Returns:
        str: The extracted text from the DOCX.
    """
    doc = docx.Document(uploaded_file)  # Create a DOCX document object
    text = "\n".join([paragraph.text for paragraph in doc.paragraphs])  # Extract text from each paragraph
    return text

def format_response(response):
    """
    Formats the response into a more presentable structure.

    Parameters:
        response (str): The raw JSON response from the model.

    Returns:
        str: The formatted response.
    """
    response_dict = json.loads(response)  # Parse the response JSON
    formatted_response = (
        f"**Job Description Match:** {response_dict['JD Match']}\n\n"  # Format JD Match
        f"**Missing Keywords:**\n- " + "\n- ".join(response_dict['MissingKeywords']) + "\n\n"  # Format missing keywords
        f"**Profile Summary:**\n{response_dict['Profile Summary']}"  # Format profile summary
    )
    return formatted_response

# Prompt Template
input_prompt = """
Hey Act Like a skilled or very experienced ATS (Application Tracking System)
with a deep understanding of tech field, software engineering, data science, data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving the resumes. Assign the percentage Matching based 
on JD and
the missing keywords with high accuracy. Provide a comprehensive list of missing keywords.
resume:{text}
description:{jd}

Return only valid JSON with this structure:
{{"JD Match": "85%", "MissingKeywords": ["keyword1", "keyword2"], "Profile Summary": "..."}}
"""

# Streamlit app interface
st.title("Smart ATS")  # Set the title of the app
st.text("Improve Your Resume ATS")  # Set the subtitle of the app
jd = st.text_area("Paste the Job Description")  # Text area for job description input
uploaded_file = st.file_uploader("Upload Your Resume", type=["pdf", "docx"], help="Please upload the PDF or Word document")  # File uploader for resume

submit = st.button("Submit")  # Submit button

if submit:
    if uploaded_file is not None:
        if uploaded_file.type == "application/pdf":
            text = input_pdf_text(uploaded_file)  # Extract text from the uploaded PDF
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            text = input_docx_text(uploaded_file)  # Extract text from the uploaded DOCX
        else:
            st.error("Unsupported file type. Please upload a PDF or DOCX file.")  # Error message for unsupported file type
            st.stop()

        prompt = input_prompt.format(text=text, jd=jd)  # Format the prompt with the extracted text and JD
        response = get_gpt_response(prompt)  # Get the model's analysis
        try:
            formatted_response = format_response(response)  # Format the response
            st.markdown(formatted_response)  # Display the formatted response
        except (json.JSONDecodeError, KeyError):
            st.error("The model returned an unexpected format. Raw reply shown below.")
            st.code(response)
    else:
        st.error("Please upload a resume.")  # Error message for missing resume
