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
```
