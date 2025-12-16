PDF AI Assistant (RAG)
A simple command‑line AI assistant that answers questions from a PDF using Retrieval‑Augmented Generation (RAG) and a local LLM via Ollama.

Features
1)Loads a PDF handbook and splits it into text chunks

2)Builds a FAISS vector index with sentence‑transformer embeddings

3)Retrieves the most relevant chunks for each question

4)Uses an Ollama model (llama3.2) to generate short answers

Chat‑style loop in the terminal (type questions, quit to exit)

Tech Stack
Python

LangChain (community components)

HuggingFace sentence-transformers/all-MiniLM-L6-v2

FAISS

Ollama (llama3.2)

How to Run
#Install Python dependencies (example):

bash
#pip install langchain-community langchain-text-splitters langchain-huggingface
#pip install sentence-transformers faiss-cpu
#Install Ollama and pull the model:

bash
ollama pull llama3.2
Put your PDF (e.g. 843_AI_Student_HandbookXI.pdf) in the same folder as rag_simple.py.

Run the chatbot:

bash
python rag_simple.py
#Then type your questions in the terminal and get answers based on the PDF.
