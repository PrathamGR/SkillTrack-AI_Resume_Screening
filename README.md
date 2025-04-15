# 📄 Skilltrack - AI Resume Screening System

Skilltrack is an AI-powered resume screening system that simplifies the hiring process by leveraging advanced text analysis and automation. This tool processes resumes, extracts key details, and matches them to job requirements. It generates structured outputs, including downloadable Excel files with candidate details, and facilitates emailing results directly to HR.

---

## 🚀 Features

### ✅ Individual Analysis
- Upload a single resume and perform **AI-powered analysis**.
- Extract detailed insights into:
  - Basic Information (Name, Email, Phone)
  - Profile Summary
  - Work Experience
  - Education
  - Technical Skills
  - Projects
  - Certificates
- Interact with the **AI-powered Q&A** system to ask questions about the resume.

### 📂 Bulk Resume Screening
- Upload multiple resumes and a job requirements file.
- Automatically identify resumes that match job requirements.
- Extract and structure key candidate information:
  - **Filename**
  - **Name**
  - **Contact (Phone)**
  - **Email**
  - **LinkedIn**
- Automatically fill missing fields with **NA** where details are not present.
- Generate a downloadable Excel sheet with auto-adjusted column widths.
- Email results directly to HR in one click.

---

## 📦 Requirements

### 🔧 Dependencies
Install the required Python libraries:
```bash
pip install streamlit pandas PyPDF2 openpyxl

⚙️ Environment Setup
Create a .env file in the root directory and add the following:

env
Copy
Edit
GROQ_API_KEY=your_api_key
EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=your_email_app_password
EMAIL_RECEIVER=hr_email@example.com
🛠️ Setup and Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/<your-repo-url>
cd skilltrack-resume-screening
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Set up environment variables in a .env file as shown above.

Run the application:

bash
Copy
Edit
streamlit run app.py
💼 How to Use
🧍 Individual Analysis
Select Individual Analysis mode from the sidebar.

Upload a resume (.pdf or .txt).

Use tabs to:

View extracted sections like Basic Info, Experience, Skills, etc.

Ask questions using the AI-powered Q&A system.

📁 Bulk Resume Screening
Select Resume Screening mode from the sidebar.

Upload:

Multiple resumes (.pdf or .txt)

One job requirements file (.pdf or .txt)

Automatically screen resumes against the job.

Download the structured Excel sheet with candidate details.

Optionally, email results directly to HR.

📤 Outputs
🧾 Excel File
Generated Excel files include the following columns:

Filename

Name

Contact (Phone)

Email

LinkedIn

Fields not found in resumes are auto-filled with NA.

📧 Email Results
Send the generated Excel file directly to HR using SMTP email integration.

🪪 License
This project is licensed under the MIT License.
