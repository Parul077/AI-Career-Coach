# 🚀 AI Career Coach
AI Career Coach is a powerful RAG-based AI web application that delivers personalized career guidance, intelligent resume evaluation, and skill gap analysis using Large Language Models (LLMs), vector search, and semantic retrieval.

The application analyzes uploaded resumes, generates structured AI-powered career insights, and allows users to interact with their resume through an intelligent question-answering system.

Built using Flask, LangChain, Groq Llama-3, Google Embeddings, and FAISS, this project demonstrates modern Generative AI application development with Retrieval-Augmented Generation (RAG).

<br>

**Live Demo:** https://ai-career-coach-1-5e5m.onrender.com/

<br>

## 🛠 Tech Stack
- **Backend**: Python, Flask
- **AI / Generative AI**: LangChain, Groq API, Llama-3.3-70B-Versatile, Prompt Engineering, Retrieval-Augmented Generation (RAG)
- **Embeddings & Vector Database**: Google Generative AI Embeddings (gemini-embedding-001), FAISS (Facebook AI Similarity Search)
- **Document Processing**: PyPDF2, Character Text Splitting
- **Frontend**: HTML, Tailwind CSS, Framer Motion
- **Deployment**: Render

<br>


## ✨ Key Features

### 📄 AI Resume Analysis

Upload a PDF resume and receive:

- Professional Summary
- Technical Skills Analysis
- Resume Evaluation
- ATS Compatibility Feedback
- Skill Gap Analysis
- Career Guidance
- Interview Readiness Suggestions
- Resume Improvement Recommendations


### 🤖 RAG-Based Resume Question Answering

Ask questions directly about your resume such as:

- "What are my strongest skills?"
- "Which career roles fit my profile?"
- "What technologies should I learn next?"
- "How can I improve my resume for ATS systems?"

The application retrieves the most relevant resume context using semantic search before generating answers.


### 🧠 Semantic Search with Vector Embeddings

The uploaded resume is:

- Extracted from PDF
- Split into text chunks
- Converted into embeddings
- Stored in a FAISS vector database

This enables accurate context-aware AI responses.


### ⚡ Fast LLM Inference

Powered by:

- Groq API
- Llama 3.3 70B Versatile Model

for fast and high-quality AI responses.


### 🎨 Modern UI/UX
- Dark modern interface
- Glassmorphism-inspired design
- Responsive layout
- Smooth user experience
- AI-generated report rendering with Markdown support

<br>

## 🧠 AI Workflow

<img width="429" height="468" alt="Screenshot 2026-05-14 114950" src="https://github.com/user-attachments/assets/aa12bba9-ce98-4e05-894c-08fbc9ad1978" />




## 🚀 Getting Started
**Prerequisites:**
- Python 3.10+
- Groq API Key
- Google AI API Key

**Installation**
Clone the repository:

```
git clone https://github.com/Parul077/AI-Career-Coach.git
cd AI-Career-Coach
```
**Create a virtual environment:**

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
**Install dependencies:**

```
pip install -r requirements.txt
```

**Configure Environment Variables:**
Create a .env file in the root directory and add your API key:

```
GROQ_API_KEY=your_groq_api_key_here
```

**Run the application:**

```
python app.py
``` 
The app will be available at http://127.0.0.1:5000.


<br>

## 📂 Project Structure
Plaintext
├── app.py                # Main Flask application logic
├── Procfile              # Deployment configuration for Render
├── requirements.txt      # Project dependencies
├── templates/            # HTML files (Index, Results, QA pages)
├── .gitignore            # Files excluded from GitHub


<br>


## 🔥 Core AI Concepts Used

**This project demonstrates practical implementation of:**

- Prompt Engineering
- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Databases
- Embeddings
- Large Language Models (LLMs)
- AI Resume Analysis
- Context-Aware Question Answering
- Generative AI Web Applications


<br>

## Project Screenshot

<img width="1890" height="820" alt="Screenshot 2026-04-08 121727" src="https://github.com/user-attachments/assets/6e31fa6c-09ba-46a8-a592-e014c4e8d5bf" />

<br>

<img width="1881" height="826" alt="Screenshot 2026-05-14 112944" src="https://github.com/user-attachments/assets/8ece85a8-dc87-42c1-818c-17462382b7fd" />

<br>

<img width="1892" height="832" alt="Screenshot 2026-05-14 115323" src="https://github.com/user-attachments/assets/5c9a5d10-c50a-4a7f-9790-5e11a7922554" />

<br>

<img width="1884" height="826" alt="Screenshot 2026-05-14 113002" src="https://github.com/user-attachments/assets/ac9b7ae6-2166-4cdd-96c6-287bfc03a5be" />

<br>

<img width="1919" height="827" alt="Screenshot 2026-04-08 124735" src="https://github.com/user-attachments/assets/f4bfb83e-2978-4e9c-8f05-913e015595d6" />

<br>

<img width="1891" height="829" alt="Screenshot 2026-04-08 124755" src="https://github.com/user-attachments/assets/bef23ada-38c1-4a79-920e-b1fe518ae229" />


<br>

## 📈 Deployment
This project is optimized for deployment on Render. Ensure you set your GROQ_API_KEY in the Render dashboard under Environment Variables before deploying.

Built with passion for the Computer Science community. 💻
