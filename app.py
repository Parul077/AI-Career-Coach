import os
from dotenv import load_dotenv
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import PyPDF2

# Core LangChain imports
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain.chains import RetrievalQA
from langchain_text_splitters import CharacterTextSplitter

# NEW: Groq and Google AI imports
from langchain_groq import ChatGroq
from langchain_google_genai import GoogleGenerativeAIEmbeddings  # Light-weight API approach
from langchain_community.vectorstores import FAISS

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# File upload configuration
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# --- WHY WE ARE NOT USING HUGGINGFACE EMBEDDINGS ---
# 1. MEMORY LIMIT: Render's Free Tier has only 512MB RAM.
# 2. HEAVY LIBRARIES: HuggingFace requires 'torch' and local model files (like all-MiniLM-L6-v2),
#    which consume ~700MB+ RAM, causing "Out of Memory" crashes.
# 3. API ADVANTAGE: GoogleGenerativeAIEmbeddings sends the text to Google's servers to get
#    the embeddings. This uses almost ZERO RAM on our server, making deployment possible.
# ----------------------------------------------------

# Initialize Google Embeddings (Uses API instead of local RAM)
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Initialize Groq LLM
llm = ChatGroq(
    temperature=0,
    model_name="llama-3.3-70b-versatile",
    groq_api_key=os.getenv("GROQ_API_KEY")
)


def perform_qa(query):
    if not os.path.exists("vector_index"):
        return "No resume has been uploaded yet. Please upload a PDF first!"

    # Load FAISS index using our new Google Embeddings
    db = FAISS.load_local("vector_index", embeddings, allow_dangerous_deserialization=True)
    retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 4})

    rqa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True
    )

    result = rqa.invoke({"query": query})
    return result['result']


def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text


text_splitter = CharacterTextSplitter(
    separator='\n',
    chunk_size=2000,
    chunk_overlap=200,
    length_function=len,
)

resume_summary_template = """
Role: You are an AI Career Coach.
Task: Given the candidate's resume, provide a comprehensive summary...
{resume}
"""

resume_prompt = PromptTemplate(
    input_variables=["resume"],
    template=resume_summary_template,
)

# Using the modern chain approach
resume_analysis_chain = resume_prompt | llm


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(url_for('index'))
    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('index'))
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        resume_text = extract_text_from_pdf(file_path)
        splitted_text = text_splitter.split_text(resume_text)

        # Create vectorstore using Google API
        vectorstore = FAISS.from_texts(splitted_text, embeddings)
        vectorstore.save_local("vector_index")

        # Invoke the chain
        response = resume_analysis_chain.invoke({"resume": resume_text})
        resume_analysis = response.content
        return render_template('results.html', resume_analysis=resume_analysis)


@app.route('/ask', methods=['GET', 'POST'])
def ask_query():
    if request.method == 'POST':
        query = request.form['query']
        result = perform_qa(query)
        return render_template('qa_results.html', query=query, result=result)
    return render_template('ask.html')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)