# 🚀 AI Career Coach
AI Career Coach is an intelligent, RAG-powered web application designed to transform your professional journey. By leveraging Large Language Models (LLMs) and advanced document retrieval, it provides instant resume evaluations, skill gap analysis, and expert career coaching tailored to your profile.

<br>

**Project Link:** https://ai-career-coach-1-5e5m.onrender.com/

<br>

## 🛠 Tech Stack
**Framework: Flask (Python)**

**AI/LLM: LangChain, Groq API (Llama-3)**

**Vector Database: FAISS (Facebook AI Similarity Search)**

**Embeddings: Hugging Face all-MiniLM-L6-v2**

**Frontend: Tailwind CSS, Framer Motion**

**Deployment: Render**

<br>


## ✨ Key Features
Automated Resume Parsing: Upload your PDF, and the AI instantly generates a structured analysis of your strengths and areas for improvement.

Interactive Career QA: Ask specific questions about your career, interview prep, or technical skill gaps based on your own resume context.

Modern UI/UX: Built with a "Glassmorphism" design aesthetic, offering a clean, professional, and intuitive experience.

Real-time Insights: Powered by fast inference from Groq and efficient vector-based retrieval.


<br>


## 🚀 Getting Started
Prerequisites
Python 3.10+
Groq API Key

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


## 📈 Deployment
This project is optimized for deployment on Render. Ensure you set your GROQ_API_KEY in the Render dashboard under Environment Variables before deploying.

Built with passion for the Computer Science community. 💻
