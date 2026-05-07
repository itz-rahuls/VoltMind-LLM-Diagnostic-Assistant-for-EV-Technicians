from app.utils.bm25 import build_bm25_index, load_bm25_index, bm25_search
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

from app.utils.pdf_loader import load_pdfs_from_folder
from app.utils.text_splitter import split_documents

DATA_PATH = "data/manuals/"
DB_PATH = "vectorstore/faiss_index"

def create_vectorstore():
    print("Loading PDFs...")
    docs = load_pdfs_from_folder(DATA_PATH)

    print(f"Loaded {len(docs)} documents")

    print("Splitting into chunks...")
    chunks = split_documents(docs)

    print(f"Created {len(chunks)} chunks")

    print("Creating embeddings...")
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    print("Building FAISS index...")
    db = FAISS.from_documents(chunks, embeddings)

    print("Saving vectorstore...")
    db.save_local(DB_PATH)

    print("Ingestion complete!")
    build_bm25_index(chunks)