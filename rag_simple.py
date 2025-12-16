from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama

print("📖 AI Handbook + Ollama RAG loading...")

# Load PDF handbook
loader = PyPDFLoader("843_AI_Student_HandbookXI.pdf")
pages = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
chunks = splitter.split_documents(pages)

# Create vector database
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = FAISS.from_documents(chunks, embeddings)

# Ollama LLM
llm = Ollama(model="llama3.2")
print("🎉 FULL RAG + OLLAMA READY!")

while True:
    question = input("\n❓ Ask (quit to exit): ").strip()
    if question.lower() in ['quit', 'exit', 'bye']:
        print("👋 RAG PROJECT COMPLETE!")
        break
    
    # Search handbook
    results = db.similarity_search(question, k=3)
    context = "\n".join([doc.page_content for doc in results])
    
    # FIXED PROMPT - இது முக்கியம்!
    answer = llm.invoke(f"""Use ONLY this handbook context to answer:

CONTEXT:
{context}

QUESTION: {question}

Answer in simple English or Tamil:""")
    
    print(f"\n🤖 {answer}\n{'='*60}")
