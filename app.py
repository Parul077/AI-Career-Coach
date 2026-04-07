import os
from dotenv import load_dotenv
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import PyPDF2

# Core LangChain imports
from langchain_core.prompts import PromptTemplate
from langchain_classic.chains import LLMChain, RetrievalQA
from langchain_text_splitters import CharacterTextSplitter

# NEW: Groq and Community imports (These usually fix the red lines)
from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# File upload configuration
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Initialize Embeddings and LLM
embeddings = HuggingFaceEmbeddings()

# Initialize Groq LLM
llm = ChatGroq(
    temperature=0,
    model_name="llama-3.3-70b-versatile",  # Or "mixtral-8x7b-32768"
    groq_api_key=os.getenv("GROQ_API_KEY")
)


def perform_qa(query):
    # Check if the folder exists locally
    if not os.path.exists("vector_index"):
        return "No resume has been uploaded yet. Please upload a PDF first!"

    db = FAISS.load_local("vector_index", embeddings, allow_dangerous_deserialization=True)
    retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 4})
    rqa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=True)

    # Use invoke instead of the deprecated __call__
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

# Note: LLMChain is deprecated in newer LangChain,
# but this will still work for now with your imports.
resume_analysis_chain = LLMChain(
    llm=llm,
    prompt=resume_prompt,
)


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

        vectorstore = FAISS.from_texts(splitted_text, embeddings)
        vectorstore.save_local("vector_index")

        # Updated to .run or .invoke
        resume_analysis = resume_analysis_chain.run(resume=resume_text)
        return render_template('results.html', resume_analysis=resume_analysis)


@app.route('/ask', methods=['GET', 'POST'])
def ask_query():
    if request.method == 'POST':
        query = request.form['query']
        result = perform_qa(query)
        return render_template('qa_results.html', query=query, result=result)
    return render_template('ask.html')


if __name__ == "__main__":
    # Get the port from Render's environment, or use 5000 for local testing
    port = int(os.environ.get("PORT", 5000))
    # '0.0.0.0' tells Flask to be visible to the outside world (Render's network)
    app.run(host="0.0.0.0", port=port)