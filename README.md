📄 Skilltrack - AI Resume Screening System
Skilltrack is an AI-powered resume screening system that simplifies the hiring process by leveraging advanced text analysis and automated features. This tool processes resumes, extracts key details, and matches them to job requirements. It produces structured outputs, including downloadable Excel files with candidate details, and even facilitates sending results via email.

Features
Individual Analysis
Upload a single resume and perform AI-powered analysis.

Extract detailed insights into:

Basic Information (Name, Email, Phone)

Profile Summary

Work Experience

Education

Technical Skills

Projects

Certificates

Interact with the AI-powered Q&A system to ask questions about the resume.

Bulk Resume Screening
Upload multiple resumes and a job requirements file.

Automatically identify resumes that meet job requirements.

Extract and structure key candidate information:

Filename

Name

Contact (Phone)

Email

LinkedIn

Missing fields are automatically filled with NA.

Download results as an Excel file with auto-adjusted column widths.

Email results to HR in one click.

Requirements
Dependencies
Install the following Python libraries:

bash
pip install streamlit pandas PyPDF2 openpyxl
Environment
Ensure that:

Groq API Key: Add your Groq API key to a .env file in the root directory.

env
GROQ_API_KEY=your_api_key
SMTP Details: Configure your sender email and app password for Gmail or another SMTP service.

Setup and Installation
Clone the repository:

bash
git clone https://github.com/<your-repo-url>
cd skilltrack-resume-screening
Install dependencies:

bash
pip install -r requirements.txt
Set the environment variable for your Groq API Key:

Create a .env file in the root directory with the following:

env
GROQ_API_KEY=your_api_key
Run the application:

bash
streamlit run app.py
How to Use
Individual Analysis
Select Individual Analysis mode from the sidebar.

Upload a resume (.pdf or .txt file).

Explore the following tabs:

AI-Powered Analysis: Ask AI questions about the resume and get detailed answers.

Resume Breakdown: View extracted sections like Basic Info, Work Experience, Education, etc.

Bulk Resume Screening
Select Resume Screening mode from the sidebar.

Upload:

Multiple resumes (.pdf or .txt files).

Job requirements file (.pdf or .txt).

Review matching resumes and download the Excel sheet with structured data.

Optionally, send results via email to HR.

Outputs
Excel File
Generated Excel files will include the following columns:

Filename

Name

Contact (Phone)

Email

LinkedIn

Email Results
Results can be emailed directly to HR via the built-in SMTP functionality.

License
This project is licensed under the MIT License.
