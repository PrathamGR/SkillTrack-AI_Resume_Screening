from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document
from utils import groq_generate


class ResumeQASystem:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50,
            separators=["\n\n", "\n", " ", ""]
        )
        self.db = None

    def create_knowledge_base(self, text: str) -> None:
        """
        Create a searchable knowledge base from resume text by splitting it into chunks.
        """
        chunks = self.text_splitter.split_text(text)
        documents = [Document(page_content=chunk) for chunk in chunks]
        self.db = FAISS.from_documents(documents, self.embeddings)

    def extract_skills(self, text: str) -> set:
        """
        Extract technical and professional skills from the provided text via LLM.
        Returns:
            A set of skills (in lowercase) parsed from the text.
        """
        prompt = f"""Extract only the technical and professional skills from this text. 
Return them as a comma-separated list.
Structure:
1. Skill-1
2. Skill-2
3. Skill-3

Do not add any additional information other than skills.
Do not include Education, Awards, Certifications, or Experience.
Text: {text}"""
        skills_text = groq_generate(prompt)
        return {skill.strip().lower() for skill in skills_text.split(',') if skill.strip()}

    def calculate_skill_match(self, required_skills: set, candidate_skills: set) -> float:
        """
        Calculate the percentage match between the required and candidate skills.
        Returns:
            The matching percentage as a float.
        """
        if not required_skills:
            return 0.0
        matched_skills = required_skills.intersection(candidate_skills)
        return len(matched_skills) / len(required_skills) * 100

    def answer_question(self, question: str) -> str:
        """
        Answer a question about the resume using semantic search over the knowledge base.
        Special handling is provided for role suitability queries.
        """
        if not self.db:
            return "Please process a resume first."

        # Retrieve relevant parts of the resume
        relevant_docs = self.db.similarity_search(question, k=4)
        context = "\n".join(doc.page_content for doc in relevant_docs)

        # Check for role suitability queries
        if self._is_role_suitability_question(question):
            return self._evaluate_role_suitability(question, context)

        # Standard prompt for general resume-related questions
        prompt = f"""You are an AI assistant helping HR professionals analyze resumes. 
Answer the following question accurately based ONLY on the information provided in the resume context.

Question: {question}

Resume Context:
{context}

Key Instructions:
1. Provide information strictly as stated in the resume context.
2. DO NOT infer or assume any details beyond the context.
3. Format your answer as bullet points for clarity.
4. If work experience durations are mentioned, calculate the total experience up to March 2025 in years and months.
5. If information is missing, state "Not mentioned in the resume."
6. For questions unrelated to resume analysis, state "I did not understand, can you please re-type the question?"

Keep your response focused, precise, and do not invent any details.
"""
        return groq_generate(prompt)

    def _is_role_suitability_question(self, question: str) -> bool:
        """
        Determine if the question pertains to the candidate's role suitability.
        """
        keywords = [
            'suitable', 'fit', 'good for', 'qualified for', 'match', 'right for',
            'appropriate for', 'good candidate for', 'consider for'
        ]
        return any(keyword in question.lower() for keyword in keywords)

    def _evaluate_role_suitability(self, question: str, context: str) -> str:
        """
        Evaluate the candidate's suitability for a role with additional context.
        This process extracts required skills from the question and compares them to 
        the candidate's skills derived from the resume context.
        """
        prompt_required = f"""Extract the required technical and professional skills or qualifications from the following question.
Return them as a comma-separated list.
Question: {question}"""
        required_skills_text = groq_generate(prompt_required)
        required_skills = {skill.strip().lower() for skill in required_skills_text.split(',') if skill.strip()}

        candidate_skills = self.extract_skills(context)
        match_percentage = self.calculate_skill_match(required_skills, candidate_skills)

        prompt = f"""Analyze the candidate's suitability for the role based on the following details:

Required Skills: {', '.join(required_skills)}
Candidate's Skills: {', '.join(candidate_skills)}
Skill Match: {match_percentage:.1f}%

Resume Context:
{context}

Provide a structured evaluation with:
- **My suggestion**: Overall assessment (indicate Strong Match, Moderate Match, or Limited Match) along with a concise 2-line summary.
- Key Matching Skills (list the top 3-4 relevant matches).
- Notable Gaps (if any).
- Additional Relevant Experience from the resume context.

Format your evaluation strictly as bullet points, referencing only information present in the resume.
"""
        return groq_generate(prompt)
